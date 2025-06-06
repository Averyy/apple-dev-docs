# GLKVector4Negate(_:)

**Framework**: GLKit  
**Kind**: func

Returns a new vector created by negating the component values of another vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector4Negate(_ vector: GLKVector4) -> GLKVector4
```

#### Return Value

A new vector.

## Parameters

- `vector`: A vector.

## See Also

- [func GLKVector4Normalize(GLKVector4) -> GLKVector4](glkvector4normalize(_:).md)
  Returns a new vector created by normalizing an input vector to a length of `1.0`.
- [func GLKVector4AddScalar(GLKVector4, Float) -> GLKVector4](glkvector4addscalar(_:_:).md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector4SubtractScalar(GLKVector4, Float) -> GLKVector4](glkvector4subtractscalar(_:_:).md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector4MultiplyScalar(GLKVector4, Float) -> GLKVector4](glkvector4multiplyscalar(_:_:).md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector4DivideScalar(GLKVector4, Float) -> GLKVector4](glkvector4dividescalar(_:_:).md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector4Add(GLKVector4, GLKVector4) -> GLKVector4](glkvector4add(_:_:).md)
  Returns the sum of two vectors.
- [func GLKVector4Subtract(GLKVector4, GLKVector4) -> GLKVector4](glkvector4subtract(_:_:).md)
  Returns the difference between two vectors.
- [func GLKVector4Multiply(GLKVector4, GLKVector4) -> GLKVector4](glkvector4multiply(_:_:).md)
  Returns the product of two vectors.
- [func GLKVector4Divide(GLKVector4, GLKVector4) -> GLKVector4](glkvector4divide(_:_:).md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector4DotProduct(GLKVector4, GLKVector4) -> Float](glkvector4dotproduct(_:_:).md)
  Returns the dot product of two vectors.
- [func GLKVector4CrossProduct(GLKVector4, GLKVector4) -> GLKVector4](glkvector4crossproduct(_:_:).md)
  Returns the cross product of two vectors.
- [func GLKVector4Lerp(GLKVector4, GLKVector4, Float) -> GLKVector4](glkvector4lerp(_:_:_:).md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector4Project(GLKVector4, GLKVector4) -> GLKVector4](glkvector4project(_:_:).md)
  Returns a new vector created by projecting a vector onto another vector.
- [func GLKVector4Maximum(GLKVector4, GLKVector4) -> GLKVector4](glkvector4maximum(_:_:).md)
  Returns a new vector whose component value at each position is the largest component value at the same position in the source vectors.
- [func GLKVector4Minimum(GLKVector4, GLKVector4) -> GLKVector4](glkvector4minimum(_:_:).md)
  Returns a new vector whose component value at each position is the smallest component value at the same position in the source vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4negate(_:))*