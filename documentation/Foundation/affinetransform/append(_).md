# append(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Mutates an affine transformation by appending another affine transform.

**Availability**:
- macOS 10.10+

## Declaration

```swift
mutating func append(_ transform: AffineTransform)
```

## Parameters

- `transform`: The affine transform that follows this transform.

## See Also

### Accumulating Tranformations
- [func rotate(byDegrees: CGFloat)](./rotate%28bydegrees%29.md)
  Mutates an affine transformation matrix to apply a rotation.
- [func rotate(byRadians: CGFloat)](./rotate%28byradians%29.md)
  Mutates an affine transformation matrix to apply a rotation.
- [func scale(CGFloat)](./scale%28_%29.md)
  Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [func scale(x: CGFloat, y: CGFloat)](./scale%28x,y%29.md)
  Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [func translate(x: CGFloat, y: CGFloat)](./translate%28x,y%29.md)
  Mutates an affine transformation matrix to perform the specified translation.
- [func prepend(AffineTransform)](./prepend%28_%29.md)
  Mutates an affine transformation by prepending another affine transform.
- [func invert()](./invert%28%29.md)
  Inverts the transformation matrix, if possible.
- [func inverted() -> AffineTransform?](./inverted%28%29.md)
  Returns an inverted version of the matrix, if possible, or nil if not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/append(_:))*