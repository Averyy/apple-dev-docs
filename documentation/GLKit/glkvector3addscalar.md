# GLKVector3AddScalar(_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new vector created by adding a scalar value to each component of a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector3AddScalar(_ vector: GLKVector3, _ value: Float) -> GLKVector3
```

#### Return Value

A new vector.

## Parameters

- `vector`: A vector.
- `value`: A scalar value.

## See Also

- [func GLKVector3Negate(GLKVector3) -> GLKVector3](glkvector3negate(_:).md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector3Normalize(GLKVector3) -> GLKVector3](glkvector3normalize(_:).md)
  Returns a new vector created by normalizing the input vector to a length of `1.0`.
- [func GLKVector3SubtractScalar(GLKVector3, Float) -> GLKVector3](glkvector3subtractscalar(_:_:).md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector3MultiplyScalar(GLKVector3, Float) -> GLKVector3](glkvector3multiplyscalar(_:_:).md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector3DivideScalar(GLKVector3, Float) -> GLKVector3](glkvector3dividescalar(_:_:).md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector3Add(GLKVector3, GLKVector3) -> GLKVector3](glkvector3add(_:_:).md)
  Returns the sum of two vectors.
- [func GLKVector3Subtract(GLKVector3, GLKVector3) -> GLKVector3](glkvector3subtract(_:_:).md)
  Returns the difference between two vectors.
- [func GLKVector3Multiply(GLKVector3, GLKVector3) -> GLKVector3](glkvector3multiply(_:_:).md)
  Returns the product of two vectors.
- [func GLKVector3Divide(GLKVector3, GLKVector3) -> GLKVector3](glkvector3divide(_:_:).md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector3DotProduct(GLKVector3, GLKVector3) -> Float](glkvector3dotproduct(_:_:).md)
  Returns the dot product of two vectors.
- [func GLKVector3CrossProduct(GLKVector3, GLKVector3) -> GLKVector3](glkvector3crossproduct(_:_:).md)
  Returns the cross product of two vectors.
- [func GLKVector3Lerp(GLKVector3, GLKVector3, Float) -> GLKVector3](glkvector3lerp(_:_:_:).md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector3Project(GLKVector3, GLKVector3) -> GLKVector3](glkvector3project(_:_:).md)
  Returns a new vector created by projecting a vector onto another vector.
- [func GLKVector3Maximum(GLKVector3, GLKVector3) -> GLKVector3](glkvector3maximum(_:_:).md)
  Returns a new vector whose component value at each position is the largest component value at the same position in the source vectors.
- [func GLKVector3Minimum(GLKVector3, GLKVector3) -> GLKVector3](glkvector3minimum(_:_:).md)
  Returns a new vector whose component value at each position is the smallest component value at the same position in the source vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector3addscalar(_:_:))*