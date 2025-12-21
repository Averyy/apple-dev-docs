# isRotatedOrScaledFromBase

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isRotatedOrScaledFromBase: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the view or any of its ancestors has had its [`frameRotation`](nsview/framerotation.md) or [`boundsRotation`](nsview/boundsrotation.md) properties modified at any time. The value is still [`true`](https://developer.apple.com/documentation/Swift/true) if the rotation factor is changed to a nonzero value and then back to 0.

Use this information to optimize drawing and coordinate calculation. Do not use it to reflect the exact state of the view’s coordinate system.

## See Also

- [func setBoundsSize(NSSize)](nsview/setboundssize(_:).md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [func scaleUnitSquare(to: NSSize)](nsview/scaleunitsquare(to:).md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.
- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func centerScanRect(NSRect) -> NSRect](nsview/centerscanrect(_:).md)
  Converts the corners of a specified rectangle to lie on the center of device pixels, which is useful in compensating for rendering overscanning when the coordinate system has been scaled.
- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var boundsRotation: CGFloat](nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [var isFlipped: Bool](nsview/isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
- [var isRotatedFromBase: Bool](nsview/isrotatedfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isrotatedorscaledfrombase)*