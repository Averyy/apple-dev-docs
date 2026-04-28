# MediaManagementAllowedMedia.Logout-eject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of volumes to eject when the user logs out.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object MediaManagementAllowedMedia.Logout-eject
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

- [object MediaManagementAllowedMedia.Mount-controls](mediamanagementallowedmedia/mount-controls-data.dictionary.md)
  A dictionary of volumes to control volume mounting.
- [object MediaManagementAllowedMedia.Unmount-controls](mediamanagementallowedmedia/unmount-controls-data.dictionary.md)
  A dictionary to control volume unmounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia/logout-eject-data.dictionary)*