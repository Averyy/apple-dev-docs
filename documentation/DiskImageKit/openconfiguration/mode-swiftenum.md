# OpenConfiguration.Mode

**Framework**: DiskImageKit  
**Kind**: enum

Open modes for disk images.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum Mode
```

## Topics

### Enumeration Cases
- [OpenConfiguration.Mode.automatic](openconfiguration/mode-swift.enum/automatic.md)
  Try to open the disk image as read-write, and fallback to read-only if there’s no read-write access.
- [OpenConfiguration.Mode.readOnly](openconfiguration/mode-swift.enum/readonly.md)
  Open the disk image in read-only mode.
- [OpenConfiguration.Mode.readWrite](openconfiguration/mode-swift.enum/readwrite.md)
  Open the disk-image with read-write permissions.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [class DiskImage](diskimage.md)
  The representation of an open disk image
- [protocol StackedImage](stackedimage.md)
  The protocol for stacked disk images that contain multiple layers.
- [protocol OpenConfigurationProtocol](openconfigurationprotocol.md)
  The protocol for disk image open configurations.
- [struct OpenConfiguration](openconfiguration.md)
  A configuration to use for opening existing disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/openconfiguration/mode-swift.enum)*