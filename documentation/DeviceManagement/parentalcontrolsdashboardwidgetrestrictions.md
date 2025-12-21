# ParentalControlsDashboardWidgetRestrictions

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures allowed dashboard widgets.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object ParentalControlsDashboardWidgetRestrictions
```

#### Discussion

Specify `com.apple.dashboard` as the payload type.

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

## Topics

### Objects
- [object ParentalControlsDashboardWidgetRestrictions.WhiteListItem](parentalcontrolsdashboardwidgetrestrictions/whitelistitem.md)
  The widget item dictionary.

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
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsdashboardwidgetrestrictions)*