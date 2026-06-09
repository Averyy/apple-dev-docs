# Managing devices and users in macOS

**Framework**: Device Management

Manage devices and users as separate entities in macOS.

#### Overview

A macOS client managed by a device management service enrolls devices and users as separate entities. Extensions to the MDM protocol in macOS enable managing the device and logged-in users independently. When enrollment occurs in this manner, the device management service receives separate requests for the device and each logged-in user.

The `mdmclient` daemon sends device requests, and the `mdmclient` agent sends user requests. If a device has multiple logged-in users, an `mdmclient` agent instance exists for each. Each agent can send requests concurrently, in addition to device requests that the daemon sends.

Devices and users have separate push tokens. The device management service uses these tokens to determine whether the device or a specific user contacts the server with an `Idle` request.

To indicate that a device management service supports both device and user connections, its device management (MDM) enrollment profile contains the string `com.apple.mdm.per-user-connections`; see [`MDM`](mdm.md) for additional information. The system promotes a device management (MDM) enrollment profile to become a device profile after installation, which has these effects:

- The device becomes a managed device.
- The local user who installs the profile becomes a managed user, and the device management service only receives requests from this user. Other local users don’t become managed users.
- Network users who log in to the device become managed users if the device management service responds successfully to their `UserAuthenticate` message. If the service won’t manage a network user, it returns a `410` HTTP status code.

During enrollment, the client sends the standard `Authenticate` request to the `CheckInURL` in the MDM payload. After that request completes, the client sends one `TokenUpdate` request for the device and another for the user performing the enrollment. The device and user connections use the same identity certificate to authenticate.

Both device and user requests contain the `UDID` key. User requests contain additional keys to help the device management service distinguish them from device requests, such as `UserLongName` and `UserShortName`.

Example of a user request:

```xml
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

The `NeedSyncResponse` key is optional. If present and `true`, the user is waiting for an MDM transaction to complete. This occurs during login while the device checks in with the device management service to ensure it has the latest settings and profiles. This key tells the service to send all commands in the current set of `Idle`/`Acknowledged`/`Error` transactions instead of relying on push notifications. During login, the client blocks the transaction only until the device management service sends an empty response to an `Idle`/`Acknowledged`/`Error` sequence.

The `UserConfiguration` key is optional. If present and `true`, the device is trying to obtain password policy settings while in Setup Assistant during device enrollment, which it uses when Setup Assistant prompts the user to create a local user account. This occurs after a device obtains device-specific settings and it receives a `DeviceConfigured` command on the device channel. If the device management service sends commands while the device is trying to obtain password policy settings, it responds with `NotNow`, because the user account doesn’t exist yet. The device continues to respond with `NotNow` until it receives a reply with no additional commands (an empty body) or it receives a `DeviceConfigured` command on the user channel. After Setup Assistant creates the user account and the user logs in, it initiates a new series of `Idle`/`Acknowledged`/`Error` transactions. At that point, the service can resend all commands and profiles, which the device processes and persists.

> **Note**:  A device can block login momentarily while it contacts the device management service for its latest settings.

Extensions to the MDM protocol also enable multiple network users to log in to a device bound to an Open Directory. For more information, see [`Enabling network and mobile user logins`](enabling-network-and-mobile-user-logins.md).

#### Create a Separate Managed Profile for Each Account

Don’t group multiple accounts together into a single profile. Create a separate profile for each account. This enables you to manage each account individually, such as to change an accountʼs settings or to remove an account when access requirements change.

Additionally, when your organization uses certificate-based account credentials, you can replace the credentials for that account as client certificates expire without needing to replace the credentials for every account.

If the password of an account has changed, your device management service can send an updated profile to the device. Conversely, if a single profile contains multiple accounts, this isn’t possible unless you keep an unencrypted copy of all of the users’ account passwords, which is insecure.

## See Also

- [Enabling network and mobile user logins](enabling-network-and-mobile-user-logins.md)
  Manage network users on macOS devices bound to an Open Directory server, and mobile users on Shared iPad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-devices-and-users-in-macos)*