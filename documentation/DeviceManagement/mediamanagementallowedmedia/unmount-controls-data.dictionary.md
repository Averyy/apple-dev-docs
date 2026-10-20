# MediaManagementAllowedMedia.Unmount-controls

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary to control volume unmounting.

**Availability**:
- macOS 10.7+ - Deprecated in 11.0

## Declaration

```
object MediaManagementAllowedMedia.Unmount-controls
```

## Properties

- `all-media` (string) *(deprecated)*: Unused; set to an empty string.

  Deprecated: macOS 11+
- `bd` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `blankbd` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `blankcd` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `blankdvd` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `cd` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `disk-image` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `dvd` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `dvdram` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `harddisk-external` ([string]) *(deprecated)*: A string or an array of media action strings. The hard disk-external category includes internally installed SD cards and USB flash drives.

  This key is the default for media types that don’t fall into other categories.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `harddisk-internal` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`
- `networkdisk` ([string]) *(deprecated)*: A media action string or an array of media action strings.

  Deprecated: macOS 11+

  **Allowed Values**: `authenticate`, `read-only`, `deny`, `eject`

## See Also

### Objects
- [object MediaManagementAllowedMedia.Logout-eject](./logout-eject-data.dictionary.md)
  A dictionary of volumes to eject when the user logs out.
- [object MediaManagementAllowedMedia.Mount-controls](./mount-controls-data.dictionary.md)
  A dictionary of volumes to control volume mounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia/unmount-controls-data.dictionary)*