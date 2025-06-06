# MediaManagementAllowedMedia.Mount-controls

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of volumes to control volume mounting.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object MediaManagementAllowedMedia.Mount-controls
```

#### Discussion

These are the valid media action strings:

`authenticate`: The user is authenticated before the media is mounted.

`read-only`: The media is mounted as read-only; this action cannot be combined with unmount controls.

`deny`: The media isn’t mounted.

`eject`: The media isn’t mounted and is ejected, if possible. Note that some volumes aren’t defined as ejectable, so using the deny key may be the best solution. This action cannot be combined with unmount controls.

## See Also

- [object MediaManagementAllowedMedia.Logout-eject](mediamanagementallowedmedia/logout-eject-data.dictionary.md)
  A dictionary of volumes to eject when the user logs out.
- [object MediaManagementAllowedMedia.Unmount-controls](mediamanagementallowedmedia/unmount-controls-data.dictionary.md)
  A dictionary to control volume unmounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mediamanagementallowedmedia/mount-controls-data.dictionary)*