# AIMAccount

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures an AIM account on the device.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AIMAccount
```

#### Discussion

Specify `com.apple.AIM.account` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | NA |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | macOS |

## Properties

- `AIMAccountDescription` (string): The description of the account.
- `AIMAuthentication` (string) *(required)*: The authentication method for the account.
- `AIMHostName` (string) *(required)*: The server address.
- `AIMPassword` (string): The user’s password.
- `AIMPort` (integer): The connection port for the server.
- `AIMUserName` (string): The user’s login name.
- `AIMUseSSL` (boolean): If `true`, enables SSL.

## See Also

- [object APN](apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload that configures a Jabber account.
- [object MacOSServerAccount](macosserveraccount.md)
  The payload that configures a macOS Server account.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlsDashboardWidgetRestrictions](parentalcontrolsdashboardwidgetrestrictions.md)
  The payload that configures allowed dashboard widgets.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/aimaccount)*