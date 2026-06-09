# MarkupAdornment.Anchor

**Framework**: PaperKit  
**Kind**: struct

The positioning reference point for an adornment within the markup canvas.

## Declaration

```swift
struct Anchor
```

## Topics

### Creating an anchor
- [static func canvas(location: CGPoint) -> MarkupAdornment.Anchor](markupadornment/anchor-swift.struct/canvas(location:).md)
  Returns an anchor at the specified location in the paper markup coordinates.
### Inspecting an anchor
- [func location(in: PaperMarkup) -> CGPoint?](markupadornment/anchor-swift.struct/location(in:).md)
  Returns the position of this anchor within the specified markup’s coordinate system.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var anchor: MarkupAdornment.Anchor](markupadornment/anchor-swift.property.md)
  The anchor that positions the adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/anchor-swift.struct)*