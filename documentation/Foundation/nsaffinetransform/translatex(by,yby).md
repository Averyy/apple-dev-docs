# translateX(by:yBy:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Applies the specified translation factors to the receiver’s transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func translateX(by deltaX: Double, yBy deltaY: Double)
```

```objc
- (void) translateXBy:(CGFloat) deltaX yBy:(CGFloat) deltaY;
```

## Discussion

Subsequent transformations cause coordinates to be shifted by `deltaX` units along the x axis and by `deltaY` units along the y axis. Translation factors do not affect `NSSize` values, which specify a differential between points.

## Parameters

- `deltaX`: The number of units to move along the x axis.
- `deltaY`: The number of units to move along the y axis.

## See Also

### Accumulating Transformations
- [func rotate(byDegrees: Double)](./rotate%28bydegrees%29.md)
  Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [func rotate(byRadians: Double)](./rotate%28byradians%29.md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](./scale%28by%29.md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func scaleX(by: Double, yBy: Double)](./scalex%28by,yby%29.md)
  Applies scaling factors to each axis of the receiver’s transformation matrix.
- [func append(NSAffineTransform)](./append%28_%29.md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](./prepend%28_%29.md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](./invert%28%29.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/translatex(by:yby:))*