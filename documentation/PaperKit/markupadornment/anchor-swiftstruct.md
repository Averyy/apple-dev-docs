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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var anchor: MarkupAdornment.Anchor](markupadornment/anchor-swift.property.md)
  The anchor that positions the adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/anchor-swift.struct)*