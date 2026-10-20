# MarkupAdornment.Anchor

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

The positioning reference point for an adornment within the markup canvas.

## Declaration

```swift
struct Anchor
```

## Topics

### Creating an anchor
- [static func canvas(location: CGPoint) -> MarkupAdornment.Anchor](./anchor-swift.struct/canvas%28location%29.md)
  Returns an anchor at the specified location in the paper markup coordinates.
### Inspecting an anchor
- [func location(in: PaperMarkup) -> CGPoint?](./anchor-swift.struct/location%28in%29.md)
  Returns the position of this anchor within the specified markup’s coordinate system.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Anchoring the adornment
- [var anchor: MarkupAdornment.Anchor](./anchor-swift.property.md)
  The anchor that positions the adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/anchor-swift.struct)*