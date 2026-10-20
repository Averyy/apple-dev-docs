# offset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The offset of the accessory from the primary pointer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
var offset: CGFloat
```

#### Discussion

This property only supports positive values.

## See Also

### Creating a custom accessory position
- [init(offset: CGFloat, angle: CGFloat)](./init%28offset,angle%29.md)
  Creates a custom accessory position with the specified offset and angle.
- [var angle: CGFloat](./angle.md)
  The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
- [static let defaultOffset: CGFloat](./defaultoffset.md)
  A constant that specifies the default offset of an accessory from the primary pointer shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointeraccessory/position-swift.struct/offset)*