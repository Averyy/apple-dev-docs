# isFlipped

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view uses a flipped coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var isFlipped: Bool { get }
```

```objc
@property (readonly, getter=isFlipped) BOOL flipped;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md), which results in a non-flipped coordinate system. In a non-flipped coordinate system, the origin is in the lower-left corner of the view and positive y-values extend upward. In a flipped coordinate system, the origin is in the upper-left corner of the view and y-values extend downward. X-values always extend to the right.

If you want your view to use a flipped coordinate system, override this property and return [`true`](../../Swift/true.md).

## See Also

### Examining Coordinate System Modifications
- [var isRotatedFromBase: Bool](./isrotatedfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds.
- [var isRotatedOrScaledFromBase: Bool](./isrotatedorscaledfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isflipped)*