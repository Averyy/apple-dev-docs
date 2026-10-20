# MarkupAdornment.ImageConfiguration

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

The visual appearance configuration for a markup adornment.

## Declaration

```swift
struct ImageConfiguration
```

#### Overview

An `ImageConfiguration` defines the visual appearance of an adornment, including the image source, size, and alignment anchor point for positioning.

## Topics

### Creating an image configuration
- [static let `default`: MarkupAdornment.ImageConfiguration](./imageconfiguration-swift.struct/default.md)
  The default image configuration using a pin-shaped system image.
- [static func systemImage(String, tint: UIColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](./imageconfiguration-swift.struct/systemimage%28_,tint,size,alignmentanchor%29-24032.md)
  Creates an image configuration using a system image.
- [static func systemImage(String, tint: NSColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](./imageconfiguration-swift.struct/systemimage%28_,tint,size,alignmentanchor%29-4itb9.md)
  Creates an image configuration using a system image.
- [static func image(UIImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](./imageconfiguration-swift.struct/image%28_,alignmentanchor%29-6ds45.md)
  Creates an image configuration using a custom image.
- [static func image(NSImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](./imageconfiguration-swift.struct/image%28_,alignmentanchor%29-6nbjc.md)
  Creates an image configuration using a custom image.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the image
- [var imageConfiguration: MarkupAdornment.ImageConfiguration](./imageconfiguration-swift.property.md)
  The image to display as the adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/imageconfiguration-swift.struct)*