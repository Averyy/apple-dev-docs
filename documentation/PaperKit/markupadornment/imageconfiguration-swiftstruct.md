# MarkupAdornment.ImageConfiguration

**Framework**: PaperKit  
**Kind**: struct

The visual appearance configuration for a markup adornment.

## Declaration

```swift
struct ImageConfiguration
```

#### Overview

An `ImageConfiguration` defines the visual appearance of an adornment, including the image source, size, and alignment anchor point for positioning.

## Topics

### Creating an image configuration
- [static let `default`: MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/default.md)
  The default image configuration using a pin-shaped system image.
- [static func systemImage(String, tint: UIColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/systemimage(_:tint:size:alignmentanchor:)-24032.md)
  Creates an image configuration using a system image.
- [static func systemImage(String, tint: NSColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/systemimage(_:tint:size:alignmentanchor:)-4itb9.md)
  Creates an image configuration using a system image.
- [static func image(UIImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/image(_:alignmentanchor:)-6ds45.md)
  Creates an image configuration using a custom image.
- [static func image(NSImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/image(_:alignmentanchor:)-6nbjc.md)
  Creates an image configuration using a custom image.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var imageConfiguration: MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.property.md)
  The image to display as the adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/imageconfiguration-swift.struct)*