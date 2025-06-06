# GLKVector2Multiply(_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new vector created by multiplying one vector by another.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector2Multiply(_ vectorLeft: GLKVector2, _ vectorRight: GLKVector2) -> GLKVector2
```

#### Return Value

A new vector whose components each represent the product of the components found in the same positions of the two source vectors.

## Parameters

- `vectorLeft`: The first vector.
- `vectorRight`: The second vector.

## See Also

- [func GLKVector2Negate(GLKVector2) -> GLKVector2](glkvector2negate(_:).md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector2Normalize(GLKVector2) -> GLKVector2](glkvector2normalize(_:).md)
  Returns a new vector created by normalizing an input vector to a length of `1.0`.
- [func GLKVector2AddScalar(GLKVector2, Float) -> GLKVector2](glkvector2addscalar(_:_:).md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector2SubtractScalar(GLKVector2, Float) -> GLKVector2](glkvector2subtractscalar(_:_:).md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector2MultiplyScalar(GLKVector2, Float) -> GLKVector2](glkvector2multiplyscalar(_:_:).md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector2DivideScalar(GLKVector2, Float) -> GLKVector2](glkvector2dividescalar(_:_:).md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector2Add(GLKVector2, GLKVector2) -> GLKVector2](glkvector2add(_:_:).md)
  Returns the sum of two vectors.
- [func GLKVector2Subtract(GLKVector2, GLKVector2) -> GLKVector2](glkvector2subtract(_:_:).md)
  Returns the difference between two vectors.
- [func GLKVector2Divide(GLKVector2, GLKVector2) -> GLKVector2](glkvector2divide(_:_:).md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector2DotProduct(GLKVector2, GLKVector2) -> Float](glkvector2dotproduct(_:_:).md)
  Returns the dot product of two vectors.
- [func GLKVector2Lerp(GLKVector2, GLKVector2, Float) -> GLKVector2](glkvector2lerp(_:_:_:).md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector2Project(GLKVector2, GLKVector2) -> GLKVector2](glkvector2project(_:_:).md)
  Returns a new vector created by projecting a vector onto another vector
- [func GLKVector2Maximum(GLKVector2, GLKVector2) -> GLKVector2](glkvector2maximum(_:_:).md)
  Returns a new vector whose component value at each position is the largest component value at the same position of the two source vectors.
- [func GLKVector2Minimum(GLKVector2, GLKVector2) -> GLKVector2](glkvector2minimum(_:_:).md)
  Returns a new vector whose component value at each position is the smallest component value at the same position of the two source vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2multiply(_:_:))*