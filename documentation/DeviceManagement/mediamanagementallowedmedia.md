# MediaManagementAllowedMedia

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures media management.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object MediaManagementAllowedMedia
```

#### Discussion

Specify `com.apple.systemuiserver` as the payload type.

This payload is deprecated as of macOS 11.

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
- [object MediaManagementAllowedMedia.Logout-eject](mediamanagementallowedmedia/logout-eject-data.dictionary.md)
  A dictionary of volumes to eject when the user logs out.
- [object MediaManagementAllowedMedia.Mount-controls](mediamanagementallowedmedia/mount-controls-data.dictionary.md)
  A dictionary of volumes to control volume mounting.
- [object MediaManagementAllowedMedia.Unmount-controls](mediamanagementallowedmedia/unmount-controls-data.dictionary.md)
  A dictionary to control volume unmounting.

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
- [object ParentalControlsDashboardWidgetRestrictions](parentalcontrolsdashboardwidgetrestrictions.md)
  The payload that configures allowed dashboard widgets.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia)*