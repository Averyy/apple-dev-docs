# isRotatedFromBase

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds.

**Availability**:
- macOS

## Declaration

```swift
var isRotatedFromBase: Bool { get }
```

```objc
@property (readonly, getter=isRotatedFromBase) BOOL rotatedFromBase;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the view or any of its ancestors has had its [`frameRotation`](./framerotation.md) or [`boundsRotation`](./boundsrotation.md) properties modified at any time. The value is still [`true`](../../Swift/true.md) if the rotation factor is changed to a nonzero value and then back to 0.

Use this information to optimize drawing and coordinate calculation. Do not use it to reflect the exact state of the view’s coordinate system.

## See Also

### Related Documentation
- [var frameRotation: CGFloat](./framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var boundsRotation: CGFloat](./boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
### Examining Coordinate System Modifications
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
- [var isRotatedOrScaledFromBase: Bool](./isrotatedorscaledfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isrotatedfrombase)*