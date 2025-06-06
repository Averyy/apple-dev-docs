# ParentalControlsDashboardWidgetRestrictions

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the parental control dashboard allow list.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ParentalControlsDashboardWidgetRestrictions
```

#### Discussion

Specify `com.apple.dashboard` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | - |

## Topics

### Objects
- [object ParentalControlsDashboardWidgetRestrictions.WhiteListItem](parentalcontrolsdashboardwidgetrestrictions/whitelistitem.md)
  The widget item dictionary.

## See Also

- [object AIMAccount](aimaccount.md)
  The payload you use to configure an AIM account on the device.
- [object APN](apn.md)
  The payload you use to configure access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload you use to configure FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload you use to configure a Jabber account.
- [object MacOSServerAccount](macosserveraccount.md)
  The payload you use to configure a macOS server account.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload you use to configure media management.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload you use to configure parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload you use to configure ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload you use to configure the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsdashboardwidgetrestrictions)*