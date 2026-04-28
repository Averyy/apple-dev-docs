# MediaManagementAllowedMedia.Unmount-controls

**Framework**: Device Management  
**Kind**: dictionary

A dictionary to control volume unmounting.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object MediaManagementAllowedMedia.Unmount-controls
```

## Properties

- `all-media` (string): Unused; set to an empty string.
- `bd` ([string]): A media action string or an array of media action strings.
- `blankbd` ([string]): A media action string or an array of media action strings.
- `blankcd` ([string]): A media action string or an array of media action strings.
- `blankdvd` ([string]): A media action string or an array of media action strings.
- `cd` ([string]): A media action string or an array of media action strings.
- `disk-image` ([string]): A media action string or an array of media action strings.
- `dvd` ([string]): A media action string or an array of media action strings.
- `dvdram` ([string]): A media action string or an array of media action strings.
- `harddisk-external` ([string]): A string or an array of media action strings. Internally installed SD cards and USB flash drives are included in the hard disk-external category. This key is the default for media types that don’t fall into other categories.
- `harddisk-internal` ([string]): A media action string or an array of media action strings.
- `networkdisk` ([string]): A media action string or an array of media action strings.

## See Also

- [object MediaManagementAllowedMedia.Logout-eject](mediamanagementallowedmedia/logout-eject-data.dictionary.md)
  A dictionary of volumes to eject when the user logs out.
- [object MediaManagementAllowedMedia.Mount-controls](mediamanagementallowedmedia/mount-controls-data.dictionary.md)
  A dictionary of volumes to control volume mounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia/unmount-controls-data.dictionary)*