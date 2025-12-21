# Enabling Network and Mobile User Logins

**Framework**: Device Management

Manage network users on macOS devices bound to an Open Directory server, and mobile users on shared iPads.

#### Overview

MDM protocol extensions enable network users to log in to a macOS device that’s bound to an Open Directory server. Upon login, these users also become managed by the MDM server with their user profiles.

A network login begins when a network user logs in; the server then issues a challenge to the device and it responds with a digest, and then the server validates the digest and issues an auth token.

##### A Network User Logs in

At login time, if the user is a network user or has a mobile home, the device issues a `UserAuthenticate` request to the server to authenticate the current user to the MDM server and obtain an `AuthToken` value. The device uses this token in subsequent requests made by this user to the server.

The authentication transaction is an HTTP `PUT` request to the `CheckInURL` address specified in the MDM enrollment-profile payload. The message body contains a property list with the following values:

| Key | Type | Content |
| --- | --- | --- |
| `MessageType` | String | `UserAuthenticate` |
| `UDID` | String | The `UDID` to use for all MDM requests for the user. |
| `UserID` | String | The local user’s `GUID`, or the network user’s `GUID` from the Open Directory record. |

##### The Server Issues a Challenge

The server response contains a dictionary with a `DigestChallenge` value that contains the standard HTTP digest. The server provides a `200` response, but a zero-length (empty) `DigestChallenge` value if it doesn’t require an `AuthToken` for this user. Otherwise, the server provides a `200` response and a non-empty `DigestChallenge` value, and the client generates a digest from the userʼs shortname, their clear-text password, and the `DigestChallenge` value.

##### The Device Sends a Digest Response

The device sends this digest in a second request to the server. This request is also sent to the `CheckInURL` specified in the MDM enrollment profile payload, and it includes the same identity used for all other MDM requests. The message body contains these values:

| Key | Type | Content |
| --- | --- | --- |
| `DigestResponse` | String | The digest that the device generates from the user’s shortname, password, and `DigestChallenge` value. |
| `MessageType` | String | `UserAuthenticate` |
| `UDID` | String | The `UDID` to use for all MDM requests for the user. |
| `UserID` | String | The local user’s `GUID`, or the network user’s `GUID` from the Open Directory record. |

##### The Server Validates the Digest to Issue an Auth Token

If the server rejects the `DigestResponse` value, for example if the password is invalid, it returns a `200` response and an empty `AuthToken` value. Otherwise, the server returns an `AuthToken` value for use by the device on subsequent requests to the server. This token remains valid until the next time the device sends a `UserAuthenticate` handshake request, which it does each time a network user logs in.

When a server rejects a `DigestResponse` value, that server returns a `410` HTTP status code to indicate it won’t manage this user. The device won’t make additional requests to the server on behalf of this user for the duration of the login session. However, the next time the user logs in, the device again sends a `UserAuthenticate` request. The server can optionally return `410` again to indicate it still won’t manage that user.

For push notifications, the device uses different push tokens for device and user connections. The device sends each token to the server using the `TokenUpdate` request. The server determines whether the token is for the device or a user based on the `UDID` and `UserID` values in the request. If the user is a network or mobile user, the server includes the `AuthToken`.

> ⚠️ **Warning**:  Push notification tokens and `AuthToken` are separate values.

##### Review a Complete Login

The following is an example of a `UserAuthenticate` transaction:

```other
// The client sends a UserAuthenticate request to the server.
<dict>
    <key>MessageType</key>
    <string>UserAuthenticate</string>
    <key>UDID</key>
    <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
    <key>UserID</key>
    <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string> 
</dict>

// The server sends a challenge.
<dict>
    <key>DigestChallenge</key>
    <string>Digest nonce="8BrAkk4GZgrG2XaDLMSSSo89VenjV5E8Se73z98RvSW7Rs",realm="fusion.home"<string>
</dict>

// The client sends a digest response.
<dict>
    <key>DigestResponse</key>
    <string>Digest username="net1",realm="fusion.home",nonce="8BrAkk4GZgrG2XaDLMSSSo89VenjV5E8Se73z98RvSW7Rs", uri="/",response="84db40bbaf5e0d49cabb0ef7d8cac369"</string>
    <key>MessageType</key>
    <string>UserAuthenticate</string>
    <key>UDID</key>
    <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
    <key>UserID</key>
    <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string> 
</dict>

// The server validates the digest response and responds with AuthToken for client session.
<key>AuthToken</key>
<string>uEOcQRJrXGbMJUDAkDZSCny5e90=</string>

// From the duration of the client login session, all requests from the network user must include the AuthToken.
<dict>
    <key>AuthToken</key>
    <string>uEOcQRJrXGbMJUDAkDZSCny5e90=</string>
    <key>Status</key>
    <string>Idle</string>
    <key>UDID</key>
    <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
    <key>UserID</key>
    <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string>
    <key>UserLongName</key>
    <string>Net One</string>
    <key>UserShortName</key>
    <string>net1</string>
</dict>
```

##### Supporting Multiple Mobile User Logins

MDM manages a shared iPad device and its users, using a similar technique to the process described above for enabling network users in macOS.

An MDM server indicates that it supports both device and user connections through Shared iPad when it includes the string `com.apple.mdm.per-user-connections` in the `ServerCapabilities` array of the MDM enrollment-profile payload. Then, when a user logs in the device sends a `TokenUpdate` request on the user channel.

The device and its users each use different push tokens. The server determines from each token it receives from a device or user whether the device or user contacts the server with an `Idle` request.

User requests contain additional values to help the server distinguish them from device requests. For more information on managing independent devices, see [`Managing MDM Devices and Users in macOS`](managing-mdm-devices-and-users-in-macos.md). However, the value for `UserID` is always set to `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` for devices, to indicate that no user authentication occurs.

To manage a user, the server stores the user push token and returns a `200` HTTP status code response. At this point, the device polls the server for a command on the user channel.

To indicate that it won’t manage the user, a server returns a `410` HTTP status code. The device won’t make additional requests to the server on behalf of this user for the duration of the login session. However, the next time the user logs in, the device again sends a `UserAuthenticate` request. The server can optionally return `410` again to indicate it still won’t manage that user.

## See Also

- [Managing MDM Devices and Users in macOS](managing-mdm-devices-and-users-in-macos.md)
  Manage devices and users as separate entities in macOS.
- [Managing Passcodes](managing-passcodes.md)
  Ensure data security by managing device passcodes and compliance with policies.
- [Dealing with Inactive MDM Devices and Invalid Push Tokens](dealing-with-inactive-mdm-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.
- [Returning a managed device to service](returning-a-managed-device-to-service.md)
  Use a device management service to return managed devices to service quickly after use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enabling-network-and-mobile-user-logins)*