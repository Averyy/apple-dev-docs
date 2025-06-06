# UIPointerAccessory.Position

**Framework**: UIKit  
**Kind**: struct

A structure that specifies the position of the accessory relative to the primary pointer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct Position
```

## Topics

### Getting an accessory position
- [static var top: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/top.md)
  An accessory position at the top of the primary pointer.
- [static var topRight: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/topright.md)
  An accessory position at the top-right of the primary pointer.
- [static var right: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/right.md)
  An accessory position at the right of the primary pointer.
- [static var bottomRight: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/bottomright.md)
  An accessory position at the bottom-right of the primary pointer.
- [static var bottom: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/bottom.md)
  An accessory position at the bottom of the primary pointer.
- [static var bottomLeft: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/bottomleft.md)
  An accessory position at the bottom-left of the primary pointer.
- [static var left: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/left.md)
  An accessory position at the left of the primary pointer.
- [static var topLeft: UIPointerAccessory.Position](uipointeraccessory/position-swift.struct/topleft.md)
  An accessory position at the top-left of the primary pointer.
### Creating a custom accessory position
- [init(offset: CGFloat, angle: CGFloat)](uipointeraccessory/position-swift.struct/init(offset:angle:).md)
  Creates a custom accessory position with the specified offset and angle.
- [var angle: CGFloat](uipointeraccessory/position-swift.struct/angle.md)
  The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
- [var offset: CGFloat](uipointeraccessory/position-swift.struct/offset.md)
  The offset of the accessory from the primary pointer.
- [static let defaultOffset: CGFloat](uipointeraccessory/position-swift.struct/defaultoffset.md)
  A constant that specifies the default offset of an accessory from the primary pointer shape.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var position: __UIPointerAccessoryPosition](uipointeraccessory/position-swift.property.md)
  The position of the accessory relative to the primary pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointeraccessory/position-swift.struct)*