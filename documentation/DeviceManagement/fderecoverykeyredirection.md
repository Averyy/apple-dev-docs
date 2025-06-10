# FDERecoveryKeyRedirection

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure FileVault recovery key redirection.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object FDERecoveryKeyRedirection
```

#### Discussion

Specify `com.apple.security.FDERecoveryRedirect` as the payload type.

Although the previous FDE Recovery payload is no longer supported in macOS 10.13 and later, it’s still supported in macOS 10.9 through 10.12. When installed, this payload causes any FDE recovery keys to be redirected to the specified URL instead of being sent to Apple. This requires sites to implement their own HTTPS server to receive the recovery keys through a POST request.

Note these cautions:

- The payload must exist in a system-scoped profile.
- Installing more than one payload of this type per machine results in an error.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

## See Also

- [object AIMAccount](aimaccount.md)
  The payload you use to configure an AIM account on the device.
- [object APN](apn.md)
  The payload you use to configure access point names.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fderecoverykeyredirection)*