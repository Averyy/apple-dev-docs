# MarkupAdornment

**Framework**: PaperKit  
**Kind**: struct

A visual adornment that appears on top of markup content within a markup view controller.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MarkupAdornment
```

#### Overview

You use a markup adornment to display an image-based overlay that you can position and configure to enhance markup content. Adornments scale with the zoom level or remain a fixed size in the base coordinate system.

## Topics

### Creating an adornment
- [init(id: UUID, anchor: MarkupAdornment.Anchor, imageConfiguration: MarkupAdornment.ImageConfiguration, dragRegion: MarkupAdornment.DragRegion, scalesWithZoom: Bool)](markupadornment/init(id:anchor:imageconfiguration:dragregion:scaleswithzoom:).md)
  Creates a new markup adornment with the specified configuration.
### Anchoring the adornment
- [MarkupAdornment.Anchor](markupadornment/anchor-swift.struct.md)
  The positioning reference point for an adornment within the markup canvas.
- [var anchor: MarkupAdornment.Anchor](markupadornment/anchor-swift.property.md)
  The anchor that positions the adornment.
### Configuring the image
- [MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct.md)
  The visual appearance configuration for a markup adornment.
- [var imageConfiguration: MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.property.md)
  The image to display as the adornment.
### Controlling interactions
- [MarkupAdornment.DragRegion](markupadornment/dragregion-swift.struct.md)
  The movement behavior and interaction constraints for a markup adornment.
- [var dragRegion: MarkupAdornment.DragRegion](markupadornment/dragregion-swift.property.md)
  The constraints that define where a person can drag this adornment.
- [var scalesWithZoom: Bool](markupadornment/scaleswithzoom.md)
  A Boolean value that indicates whether the adornment scales with the zoom level or remains fixed in the base coordinate system.
### Identifying markup
- [var id: UUID](markupadornment/id.md)
  A unique identifier for this adornment.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment)*