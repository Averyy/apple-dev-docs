# GLKVector3SubtractScalar(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a new vector created by subtracting a scalar value from each component of a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector3SubtractScalar(_ vector: GLKVector3, _ value: Float) -> GLKVector3
```

```c
static GLKVector3 GLKVector3SubtractScalar(GLKVector3 vector, float value);
```

## Return Value

A new vector.

## Parameters

- `vector`: A vector.
- `value`: A scalar value.

## See Also

### Mathematical Operations Performed on Vectors
- [func GLKVector3Negate(GLKVector3) -> GLKVector3](./glkvector3negate%28_%29.md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector3Normalize(GLKVector3) -> GLKVector3](./glkvector3normalize%28_%29.md)
  Returns a new vector created by normalizing the input vector to a length of `1.0`.
- [func GLKVector3AddScalar(GLKVector3, Float) -> GLKVector3](./glkvector3addscalar%28_,_%29.md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector3MultiplyScalar(GLKVector3, Float) -> GLKVector3](./glkvector3multiplyscalar%28_,_%29.md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector3DivideScalar(GLKVector3, Float) -> GLKVector3](./glkvector3dividescalar%28_,_%29.md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector3Add(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3add%28_,_%29.md)
  Returns the sum of two vectors.
- [func GLKVector3Subtract(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3subtract%28_,_%29.md)
  Returns the difference between two vectors.
- [func GLKVector3Multiply(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3multiply%28_,_%29.md)
  Returns the product of two vectors.
- [func GLKVector3Divide(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3divide%28_,_%29.md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector3DotProduct(GLKVector3, GLKVector3) -> Float](./glkvector3dotproduct%28_,_%29.md)
  Returns the dot product of two vectors.
- [func GLKVector3CrossProduct(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3crossproduct%28_,_%29.md)
  Returns the cross product of two vectors.
- [func GLKVector3Lerp(GLKVector3, GLKVector3, Float) -> GLKVector3](./glkvector3lerp%28_,_,_%29.md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector3Project(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3project%28_,_%29.md)
  Returns a new vector created by projecting a vector onto another vector.
- [func GLKVector3Maximum(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3maximum%28_,_%29.md)
  Returns a new vector whose component value at each position is the largest component value at the same position in the source vectors.
- [func GLKVector3Minimum(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3minimum%28_,_%29.md)
  Returns a new vector whose component value at each position is the smallest component value at the same position in the source vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector3subtractscalar(_:_:))*