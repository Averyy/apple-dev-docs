# OpenConfiguration

**Framework**: DiskImageKit  
**Kind**: struct

A configuration to use for opening existing disk images.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct OpenConfiguration
```

## Topics

### Initializers
- [init(url: URL, mode: OpenConfiguration.Mode)](openconfiguration/init(url:mode:).md)
  Creates a configuration for opening a disk image.
### Instance Properties
- [let mode: OpenConfiguration.Mode](openconfiguration/mode-swift.property.md)
  The mode in which to open the disk image.
- [let url: URL](openconfiguration/url.md)
  The URL of the disk image to open.
### Enumerations
- [OpenConfiguration.Mode](openconfiguration/mode-swift.enum.md)
  Open modes for disk images.

## Relationships

### Conforms To
- [OpenConfigurationProtocol](openconfigurationprotocol.md)

## See Also

- [class DiskImage](diskimage.md)
  The representation of an open disk image
- [protocol StackedImage](stackedimage.md)
  The protocol for stacked disk images that contain multiple layers.
- [protocol OpenConfigurationProtocol](openconfigurationprotocol.md)
  The protocol for disk image open configurations.
- [OpenConfiguration.Mode](openconfiguration/mode-swift.enum.md)
  Open modes for disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/openconfiguration)*