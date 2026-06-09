# MediaManagementAllowedMedia.Unmount-controls

**Framework**: Device Management  
**Kind**: dictionary

A dictionary to control volume unmounting.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object MediaManagementAllowedMedia.Unmount-controls
```

## Properties

- `all-media` (string): Unused; set to an empty string. Deprecated: macOS 11+
- `bd` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `blankbd` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `blankcd` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `blankdvd` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `cd` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `disk-image` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `dvd` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `dvdram` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `harddisk-external` ([string]): A string or an array of media action strings. The hard disk-external category includes internally installed SD cards and USB flash drives. This key is the default for media types that don’t fall into other categories. Deprecated: macOS 11+
- `harddisk-internal` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+
- `networkdisk` ([string]): A media action string or an array of media action strings. Deprecated: macOS 11+

## See Also

- [object MediaManagementAllowedMedia.Logout-eject](mediamanagementallowedmedia/logout-eject-data.dictionary.md)
  A dictionary of volumes to eject when the user logs out.
- [object MediaManagementAllowedMedia.Mount-controls](mediamanagementallowedmedia/mount-controls-data.dictionary.md)
  A dictionary of volumes to control volume mounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia/unmount-controls-data.dictionary)*