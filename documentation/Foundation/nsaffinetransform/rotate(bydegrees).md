# rotate(byDegrees:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func rotate(byDegrees angle: Double)
```

```objc
- (void) rotateByDegrees:(CGFloat) angle;
```

## Discussion

After invoking this method, applying the receiver’s matrix turns the axes counterclockwise about the current origin by `angle` degrees, in addition to performing all previous transformations.

## Parameters

- `angle`: The rotation angle, measured in degrees.

## See Also

### Accumulating Transformations
- [func rotate(byRadians: Double)](./rotate%28byradians%29.md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](./scale%28by%29.md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func scaleX(by: Double, yBy: Double)](./scalex%28by,yby%29.md)
  Applies scaling factors to each axis of the receiver’s transformation matrix.
- [func translateX(by: Double, yBy: Double)](./translatex%28by,yby%29.md)
  Applies the specified translation factors to the receiver’s transformation matrix.
- [func append(NSAffineTransform)](./append%28_%29.md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](./prepend%28_%29.md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](./invert%28%29.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/rotate(bydegrees:))*