# isRotatedOrScaledFromBase

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var isRotatedOrScaledFromBase: Bool { get }
```

```objc
@property (readonly, getter=isRotatedOrScaledFromBase) BOOL rotatedOrScaledFromBase;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the view or any of its ancestors has had its [`frameRotation`](./framerotation.md) or [`boundsRotation`](./boundsrotation.md) properties modified at any time. The value is still [`true`](../../Swift/true.md) if the rotation factor is changed to a nonzero value and then back to 0.

Use this information to optimize drawing and coordinate calculation. Do not use it to reflect the exact state of the view’s coordinate system.

## See Also

### Related Documentation
- [func setBoundsSize(NSSize)](./setboundssize%28_%29.md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [func scaleUnitSquare(to: NSSize)](./scaleunitsquare%28to%29.md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.
- [var bounds: NSRect](./bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func centerScanRect(NSRect) -> NSRect](./centerscanrect%28_%29.md)
  Converts the corners of a specified rectangle to lie on the center of device pixels, which is useful in compensating for rendering overscanning when the coordinate system has been scaled.
- [var frameRotation: CGFloat](./framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var boundsRotation: CGFloat](./boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
### Examining Coordinate System Modifications
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
- [var isRotatedFromBase: Bool](./isrotatedfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isrotatedorscaledfrombase)*