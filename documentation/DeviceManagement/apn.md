# APN

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure access point names.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+

## Declaration

```swift
object APN
```

#### Discussion

Specify `com.apple.apn.managed` as the payload type.

This profile is deprecated. Use the [`Cellular`](cellular.md) profile instead.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Allow manual install | iOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

## Topics

### Objects
- [object APN.DefaultsData](apn/defaultsdata-data.dictionary.md)
  An array of access point name dictionaries.

## See Also

- [object AIMAccount](aimaccount.md)
  The payload you use to configure an AIM account on the device.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload you use to configure FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload you use to configure a Jabber account.
- [object MacOSServerAccount](macosserveraccount.md)
  The payload you use to configure a macOS server account.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload you use to configure media management.
- [object ParentalControlsDashboardWidgetRestrictions](parentalcontrolsdashboardwidgetrestrictions.md)
  The payload you use to configure the parental control dashboard allow list.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload you use to configure parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload you use to configure ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload you use to configure the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apn)*