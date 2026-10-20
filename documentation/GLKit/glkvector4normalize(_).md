# GLKVector4Normalize(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a new vector created by normalizing an input vector to a length of `1.0`.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector4Normalize(_ vector: GLKVector4) -> GLKVector4
```

```c
static GLKVector4 GLKVector4Normalize(GLKVector4 vector);
```

#### Return Value

A new vector.

#### Discussion

The resulting vector points in the same direction as the input vector, but has a length of `1.0`.

## Parameters

- `vector`: A vector.

## See Also

### Mathematical Operations Performed on Vectors
- [func GLKVector4Negate(GLKVector4) -> GLKVector4](./glkvector4negate%28_%29.md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector4AddScalar(GLKVector4, Float) -> GLKVector4](./glkvector4addscalar%28_,_%29.md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector4SubtractScalar(GLKVector4, Float) -> GLKVector4](./glkvector4subtractscalar%28_,_%29.md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector4MultiplyScalar(GLKVector4, Float) -> GLKVector4](./glkvector4multiplyscalar%28_,_%29.md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector4DivideScalar(GLKVector4, Float) -> GLKVector4](./glkvector4dividescalar%28_,_%29.md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector4Add(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4add%28_,_%29.md)
  Returns the sum of two vectors.
- [func GLKVector4Subtract(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4subtract%28_,_%29.md)
  Returns the difference between two vectors.
- [func GLKVector4Multiply(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4multiply%28_,_%29.md)
  Returns the product of two vectors.
- [func GLKVector4Divide(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4divide%28_,_%29.md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector4DotProduct(GLKVector4, GLKVector4) -> Float](./glkvector4dotproduct%28_,_%29.md)
  Returns the dot product of two vectors.
- [func GLKVector4CrossProduct(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4crossproduct%28_,_%29.md)
  Returns the cross product of two vectors.
- [func GLKVector4Lerp(GLKVector4, GLKVector4, Float) -> GLKVector4](./glkvector4lerp%28_,_,_%29.md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector4Project(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4project%28_,_%29.md)
  Returns a new vector created by projecting a vector onto another vector.
- [func GLKVector4Maximum(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4maximum%28_,_%29.md)
  Returns a new vector whose component value at each position is the largest component value at the same position in the source vectors.
- [func GLKVector4Minimum(GLKVector4, GLKVector4) -> GLKVector4](./glkvector4minimum%28_,_%29.md)
  Returns a new vector whose component value at each position is the smallest component value at the same position in the source vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4normalize(_:))*