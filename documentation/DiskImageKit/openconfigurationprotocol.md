# OpenConfigurationProtocol

**Framework**: DiskImageKit  
**Kind**: protocol

The protocol for disk image open configurations.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol OpenConfigurationProtocol
```

#### Overview

This protocol defines the common requirements for opening disk images. Conforming types can be used with [`init(opening:)`](diskimage/init(opening:).md).

## Topics

### Instance Properties
- [var mode: OpenConfiguration.Mode](openconfigurationprotocol/mode.md)
  The [`OpenConfiguration.Mode`](openconfiguration/mode-swift.enum.md) in which to open the disk image.
- [var url: URL](openconfigurationprotocol/url.md)
  The URL of the disk image to open.
### Type Methods
- [static func open(url: URL, mode: OpenConfiguration.Mode) -> Self](openconfigurationprotocol/open(url:mode:).md)
  Returns a configuration to use for opening a disk image.

## Relationships

### Conforming Types
- [OpenConfiguration](openconfiguration.md)

## See Also

- [class DiskImage](diskimage.md)
  The representation of an open disk image
- [protocol StackedImage](stackedimage.md)
  The protocol for stacked disk images that contain multiple layers.
- [struct OpenConfiguration](openconfiguration.md)
  A configuration to use for opening existing disk images.
- [OpenConfiguration.Mode](openconfiguration/mode-swift.enum.md)
  Open modes for disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/openconfigurationprotocol)*