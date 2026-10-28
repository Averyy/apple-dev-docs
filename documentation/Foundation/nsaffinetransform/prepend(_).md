# prepend(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Prepends the specified matrix to the receiver’s matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

*Mac Catalyst*

```swift
func prepend(_ transform: NSAffineTransform)
```

*macOS*

```swift
func prepend(_ transform: AffineTransform)
```

```objc
- (void) prependTransform:(NSAffineTransform *) transform;
```

## Discussion

This method multiplies the matrix in `transform` by the receiver’s matrix and replaces the receiver’s matrix with the result. This type of operation is the same as applying the transformations in `transform` followed by the transformations in the receiver.

## Parameters

- `transform`: The matrix to prepend to the receiver.

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
- [func append(NSAffineTransform)](./append%28_%29.md)
  Appends the specified matrix to the receiver’s matrix.
- [func invert()](./invert%28%29.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/prepend(_:))*