# scaleX(by:yBy:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Applies scaling factors to each axis of the receiver’s transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func scaleX(by scaleX: Double, yBy scaleY: Double)
```

```objc
- (void) scaleXBy:(CGFloat) scaleX yBy:(CGFloat) scaleY;
```

## Discussion

After invoking this method, applying the receiver’s matrix modifies the unit length on the x axis by a factor of `scaleX` and the y axis by a factor of `scaleY`, in addition to performing all previous transformations. A value of 1.0 for either axis scales the content on that axis to the same size.

## Parameters

- `scaleX`: The scaling factor to apply to the x axis.
- `scaleY`: The scaling factor to apply to the y axis.

## See Also

### Accumulating Transformations
- [func rotate(byDegrees: Double)](./rotate%28bydegrees%29.md)
  Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [func rotate(byRadians: Double)](./rotate%28byradians%29.md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](./scale%28by%29.md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func translateX(by: Double, yBy: Double)](./translatex%28by,yby%29.md)
  Applies the specified translation factors to the receiver’s transformation matrix.
- [func append(NSAffineTransform)](./append%28_%29.md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](./prepend%28_%29.md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](./invert%28%29.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/scalex(by:yby:))*