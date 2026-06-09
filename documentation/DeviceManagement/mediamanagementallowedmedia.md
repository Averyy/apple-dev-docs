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
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

## Topics

### Objects
- [object MediaManagementAllowedMedia.Logout-eject](mediamanagementallowedmedia/logout-eject-data.dictionary.md)
  A dictionary of volumes to eject when the user logs out.
- [object MediaManagementAllowedMedia.Mount-controls](mediamanagementallowedmedia/mount-controls-data.dictionary.md)
  A dictionary of volumes to control volume mounting.
- [object MediaManagementAllowedMedia.Unmount-controls](mediamanagementallowedmedia/unmount-controls-data.dictionary.md)
  A dictionary to control volume unmounting.

## Properties

- `logout-eject` (MediaManagementAllowedMedia.Logout-eject): The media type dictionary that defines volumes to eject when the user logs out. Deprecated: macOS 11+
- `mount-controls` (MediaManagementAllowedMedia.Mount-controls): The media type dictionary that controls volume mounting. Deprecated: macOS 11+
- `unmount-controls` (MediaManagementAllowedMedia.Unmount-controls): The media type dictionary that controls volume unmounting. Deprecated: macOS 11+

## See Also

- [object APN](apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia)*