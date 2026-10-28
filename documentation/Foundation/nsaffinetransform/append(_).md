# append(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends the specified matrix to the receiver’s matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

*Mac Catalyst*

```swift
func append(_ transform: NSAffineTransform)
```

*macOS*

```swift
func append(_ transform: AffineTransform)
```

```objc
- (void) appendTransform:(NSAffineTransform *) transform;
```

## Discussion

This method multiplies the receiver’s matrix by the matrix in `aTransform` and replaces the receiver’s matrix with the results. This type of operation is the same as applying the transformations in the receiver followed by the transformations in `aTransform`.

## Parameters

- `transform`: The matrix to append to the receiver.

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
- [func translateX(by: Double, yBy: Double)](./translatex%28by,yby%29.md)
  Applies the specified translation factors to the receiver’s transformation matrix.
- [func prepend(NSAffineTransform)](./prepend%28_%29.md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](./invert%28%29.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/append(_:))*