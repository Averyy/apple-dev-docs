# ShareKit

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures ShareKit.

**Availability**:
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ShareKit
```

#### Discussion

Specify `com.apple.ShareKitHelper` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

## Properties

- `SHKAllowedShareServices` ([string]): The list of plugin IDs that show up in the user’s Share menu. If this array exists, only these items are permitted.
- `SHKDeniedShareServices` ([string]): The list of plugin IDs that won’t show up in the user’s Share menu. This key is used only if there is no `SHKAllowedShareServices` key.

## See Also

- [object AIMAccount](aimaccount.md)
  The payload that configures an AIM account on the device.
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
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/sharekit)*