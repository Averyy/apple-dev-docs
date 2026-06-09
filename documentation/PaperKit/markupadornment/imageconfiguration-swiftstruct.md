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
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var imageConfiguration: MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.property.md)
  The image to display as the adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/imageconfiguration-swift.struct)*