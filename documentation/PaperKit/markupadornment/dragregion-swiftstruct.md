# MarkupAdornment.DragRegion

**Framework**: PaperKit  
**Kind**: struct

The movement behavior and interaction constraints for a markup adornment.

## Declaration

```swift
struct DragRegion
```

#### Overview

A `DragRegion` determines if and how people can reposition an adornment within the markup canvas. You can configure adornments to remain fixed in place or allow people to move them freely.

## Topics

### Choosing a drag region
- [static let fixed: MarkupAdornment.DragRegion](markupadornment/dragregion-swift.struct/fixed.md)
  A drag region that prevents people from moving the adornment.
- [static let canvas: MarkupAdornment.DragRegion](markupadornment/dragregion-swift.struct/canvas.md)
  A drag region that allows people to move the adornment within the canvas.

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

- [var dragRegion: MarkupAdornment.DragRegion](markupadornment/dragregion-swift.property.md)
  The constraints that define where a person can drag this adornment.
- [var scalesWithZoom: Bool](markupadornment/scaleswithzoom.md)
  A Boolean value that indicates whether the adornment scales with the zoom level or remains fixed in the base coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/dragregion-swift.struct)*