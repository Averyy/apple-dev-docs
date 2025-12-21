# isRotatedFromBase

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isRotatedFromBase: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the view or any of its ancestors has had its [`frameRotation`](nsview/framerotation.md) or [`boundsRotation`](nsview/boundsrotation.md) properties modified at any time. The value is still [`true`](https://developer.apple.com/documentation/Swift/true) if the rotation factor is changed to a nonzero value and then back to 0.

Use this information to optimize drawing and coordinate calculation. Do not use it to reflect the exact state of the view’s coordinate system.

## See Also

- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var boundsRotation: CGFloat](nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [var isFlipped: Bool](nsview/isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
- [var isRotatedOrScaledFromBase: Bool](nsview/isrotatedorscaledfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isrotatedfrombase)*