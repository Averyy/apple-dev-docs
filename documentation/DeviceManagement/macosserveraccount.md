# MacOSServerAccount

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a macOS server account.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Declaration

```swift
object MacOSServerAccount
```

#### Discussion

Specify `com.apple.osxserver.account` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | NA |
| Allow manual install | iOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | iOS |

## Topics

### Objects
- [object MacOSServerAccount.ConfiguredAccountsItem](macosserveraccount/configuredaccountsitem.md)
  An array of dictionaries containing configured account types and relevant settings

## See Also

- [object AIMAccount](aimaccount.md)
  The payload you use to configure an AIM account on the device.
- [object APN](apn.md)
  The payload you use to configure access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload you use to configure FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload you use to configure a Jabber account.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/macosserveraccount)*