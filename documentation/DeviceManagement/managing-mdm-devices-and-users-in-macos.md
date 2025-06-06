# Managing MDM Devices and Users in macOS

**Framework**: Device Management

Manage devices and users as separate entities in macOS.

#### Overview

A macOS client on an MDM server enrolls devices and users as separate entities. Extensions to the MDM protocol in macOS enable managing the device and logged-in users independently. When enrollment occurs in this manner, the MDM server receives separate requests for the device and each logged-in user.

The `mdmclient` daemon sends device requests, and the `mdmclient` agent sends user requests. If a device has multiple logged-in users, an `mdmclient` agent instance exists for each. Each agent can send requests concurrently, in addition to device requests that the daemon sends.

Devices and users have separate push tokens. The server uses these tokens to determine whether the device or a specific user contacts the server with an `Idle` request.

To indicate that an MDM server supports both device and user connections, its enrollment profile payload contains the string `com.apple.mdm.per-user-connections`; see [`MDM`](mdm.md) for additional information. The system promotes an MDM enrollment profile to become a device profile after installation, which has these effects:

- The device becomes a managed device.
- The local user who installs the profile becomes a managed user, and the server only receives requests from this user. Other local users don’t become managed users.
- Network users who log in to the device become managed users if the server responds successfully to their `UserAuthenticate` message. If the server won’t manage a network user, it returns a `410` HTTP status code.

During enrollment, the client sends the standard `Authenticate` request to the `CheckInURL` in the MDM payload. After that request completes, the client sends one `TokenUpdate` request for the device and another for the user performing the enrollment. The device and user connections use the same client certificate to authenticate.

Both device and user requests contain the `UDID` key. User requests contain additional keys to help the server distinguish them from device requests, such as `UserLongName` and `UserShortName`.

Example of a User Request

```other
<key>UDID</key>
<string>23EB7CD8-5567-5E97-827F-06E4E4C456B2</string>
<key>UserID</key>
<string>F17C470A-3ADC-47EC-A7CC-D432867F4793</string>
<key>UserLongName</key>
<string>Jimmy Smith</string>
<key>UserShortName</key>
<string>jimmys</string>
<key>NeedSyncResponse</key>
<boolean>true</boolean>
```

`NeedSyncResponse` is optional. If present and `true`, the user is waiting for an MDM transaction to complete. This occurs during login while the device checks in with the MDM server to ensure it has the latest settings and profiles. This key tells the server to send all commands in the current set of `Idle`/`Acknowledged`/`Error` transactions instead of relying on push notifications. During login, the client blocks the transaction only until the server sends an empty response to an `Idle`/`Acknowledged`/`Error` sequence.

`UserConfiguration` is optional. If present and `true`, the device is trying to obtain password policy settings while in Setup Assistant during device enrollment, which it uses when Setup Assistant prompts the user to create a local user account. This occurs after a device obtains device-specific settings and it receives a `DeviceConfigured` command on the device channel. If the server sends commands while the device is trying to obtain password policy settings, it responds with `NotNow`, because the user account doesn’t exist yet. The device continues to respond with `NotNow` until it receives a reply with no additional commands (an empty body) or it receives a `DeviceConfigured` command on the user channel. After Setup Assistant creates the user account and the user logs in, it initiates a new series of `Idle`/`Acknowledged`/`Error` transactions. At that point, the server can resend all commands and profiles, which the device processes and persists.

> **Note**:  A device can block login momentarily while it contacts the MDM server for its latest settings.

 A device can block login momentarily while it contacts the MDM server for its latest settings.

Extensions to the MDM protocol also enable multiple network users to log in to a device that an MDM admin binds to an Open Directory. For more information, see [`Enabling Network and Mobile User Logins`](enabling-network-and-mobile-user-logins.md).

##### Create a Separate Managed Profile for Each Account

Don’t group multiple accounts together into a single profile. Create a separate profile for each account. This enables you to manage each account individually, such as to change an accountʼs settings or to remove an account when access requirements change.

Additionally, when your organization uses certificate-based account credentials, you can replace the credentials for that account as client certificates expire without needing to replace the credentials for every account.

If a user requests a password change for an account, your servers can update the password on the device. Conversely, if a single profile contains multiple accounts, this isn’t possible unless the server keeps an unencrypted copy of all of the users’ account passwords, which is insecure.

## See Also

- [Enabling Network and Mobile User Logins](enabling-network-and-mobile-user-logins.md)
  Manage network users on macOS devices bound to an Open Directory server, and mobile users on shared iPads.
- [Managing Passcodes](managing-passcodes.md)
  Ensure data security by managing device passcodes and compliance with policies.
- [Dealing with Inactive MDM Devices and Invalid Push Tokens](dealing-with-inactive-mdm-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-mdm-devices-and-users-in-macos)*