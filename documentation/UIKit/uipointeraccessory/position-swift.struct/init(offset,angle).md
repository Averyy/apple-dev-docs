# init(offset:angle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a custom accessory position with the specified offset and angle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
init(offset: CGFloat = Position.defaultOffset, angle: CGFloat = 0)
```

## See Also

### Creating a custom accessory position
- [var angle: CGFloat](./angle.md)
  The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
- [var offset: CGFloat](./offset.md)
  The offset of the accessory from the primary pointer.
- [static let defaultOffset: CGFloat](./defaultoffset.md)
  A constant that specifies the default offset of an accessory from the primary pointer shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointeraccessory/position-swift.struct/init(offset:angle:))*