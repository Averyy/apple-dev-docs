# Enabling network and mobile user logins

**Framework**: Device Management

Manage network users on macOS devices bound to an Open Directory server, and mobile users on Shared iPad.

#### Overview

MDM protocol extensions enable network users to log in to a macOS device that’s bound to an Open Directory server. Upon login, these users also become managed by the device management service with their user profiles.

A network login begins when a network user logs in; the device management service then issues a challenge to the device and it responds with a digest, and then the service validates the digest and issues an authentication token.

#### Log in a Network User

At login time, if the user is a network user or has a mobile home, the device issues a `UserAuthenticate` request to the device management service to authenticate the current user to the service and obtain an `AuthToken` value. The device uses this token in subsequent requests made by this user to the device management service.

The authentication transaction is an HTTP `PUT` request to the `CheckInURL` address specified in the device management (MDM) enrollment profile. The message body contains a property list with the following values:

| Key | Type | Content |
| --- | --- | --- |
| `MessageType` | String | `UserAuthenticate` |
| `UDID` | String | The `UDID` to use for all management requests for the user. |
| `UserID` | String | The local user’s `GUID`, or the network user’s `GUID` from the Open Directory record. |

#### Issue a Challenge

The device management service response contains a dictionary with a `DigestChallenge` value that contains the standard HTTP digest. The service provides a `200` response, but a zero-length (empty) `DigestChallenge` value if it doesn’t require an `AuthToken` for this user. Otherwise, the device management service provides a `200` response and a non-empty `DigestChallenge` value, and the client generates a digest from the userʼs shortname, their clear-text password, and the `DigestChallenge` value.

#### Send a Digest Response

The device sends this digest in a second request to the device management service. This request is also sent to the `CheckInURL` specified in the device management (MDM) enrollment profile, and it includes the same identity used for all other management requests. The message body contains these values:

| Key | Type | Content |
| --- | --- | --- |
| `DigestResponse` | String | The digest that the device generates from the user’s shortname, password, and `DigestChallenge` value. |
| `MessageType` | String | `UserAuthenticate` |
| `UDID` | String | The `UDID` to use for all management requests for the user. |
| `UserID` | String | The local user’s `GUID`, or the network user’s `GUID` from the Open Directory record. |

#### Validate the Digest to Issue an Authentication Token

If the device management service rejects the `DigestResponse` value, for example if the password is invalid, it returns a `200` response and an empty `AuthToken` value. Otherwise, the service returns an `AuthToken` value for use by the device on subsequent requests to the device management service. This token remains valid until the next time the device sends a `UserAuthenticate` handshake request, which it does each time a network user logs in.

When a device management service rejects a `DigestResponse` value, that service returns a `410` HTTP status code to indicate it won’t manage this user. The device won’t make additional requests to the service on behalf of this user for the duration of the login session. However, the next time the user logs in, the device again sends a `UserAuthenticate` request again. The device management service can again optionally return `410` again to indicate it still won’t manage that user.

For push notifications, the device uses different push tokens for device and user connections. The device sends each token to the device management service using the `TokenUpdate` request. The service determines whether the token is for the device or a user based on the `UDID` and `UserID` values in the request. If the user is a network or mobile user, the service includes the `AuthToken`.

> ⚠️ **Warning**:  Push notification tokens and `AuthToken` are separate values.

#### Review a Complete Login

The following is an example of a `UserAuthenticate` transaction:

```xml
// The client sends a UserAuthenticate request to the device management service.
<dict>
    <key>MessageType</key>
    <string>UserAuthenticate</string>
    <key>UDID</key>
    <string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
    <key>UserID</key>
    <string>16C0477E-EB2F-4B5E-AAFD-92B2B91C4B16</string> 
</dict>

// The device management service sends a challenge.
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

// The service validates the digest response and responds with AuthToken for a client session.
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

#### Support Multiple Users on Ipad

A device management service manages a Shared iPad and its users using a similar technique to the process described above for enabling network users in macOS.

A device management service indicates that it supports both device and user connections through Shared iPad when it includes the string `com.apple.mdm.per-user-connections` in the `ServerCapabilities` array of the device management (MDM) enrollment profile. Then, when a user logs in the device sends a `TokenUpdate` request on the user channel.

The device and its users each use different push tokens. The device management service determines from each token it receives from a device or user whether the device or user contacts the service with an `Idle` request.

User requests contain additional values to help the device management service distinguish them from device requests. However, the value for `UserID` is always set to `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` for devices, to indicate that no user authentication occurs. For more information on managing independent devices, see [`Managing devices and users in macOS`](managing-devices-and-users-in-macos.md).

To manage a user, the device management service stores the user push token and returns a `200` HTTP status code response. At this point, the device polls the service for a command on the user channel.

To indicate that it won’t manage the user, a device management service returns a `410` HTTP status code. The device won’t make additional requests to the service on behalf of this user for the duration of the login session. However, the next time the user logs in, the device again sends a `UserAuthenticate` request. The service can optionally return `410` again to indicate it still won’t manage that user.

## See Also

- [Managing devices and users in macOS](managing-devices-and-users-in-macos.md)
  Manage devices and users as separate entities in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enabling-network-and-mobile-user-logins)*