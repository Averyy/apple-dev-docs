# GLKVector2AllGreaterThanScalar(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector2AllGreaterThanScalar(_ vector: GLKVector2, _ value: Float) -> Bool
```

```c
static bool GLKVector2AllGreaterThanScalar(GLKVector2 vector, float value);
```

#### Return Value

[`true`](../Swift/true.md) if all of the vector’s components are greater than the scalar value, [`false`](../Swift/false.md) otherwise.

## Parameters

- `vector`: A vector.
- `value`: A scalar.

## See Also

### Comparison Operations
- [func GLKVector2AllEqualToScalar(GLKVector2, Float) -> Bool](./glkvector2allequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.
- [func GLKVector2AllEqualToVector2(GLKVector2, GLKVector2) -> Bool](./glkvector2allequaltovector2%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.
- [func GLKVector2AllGreaterThanOrEqualToScalar(GLKVector2, Float) -> Bool](./glkvector2allgreaterthanorequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector2AllGreaterThanOrEqualToVector2(GLKVector2, GLKVector2) -> Bool](./glkvector2allgreaterthanorequaltovector2%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector2AllGreaterThanVector2(GLKVector2, GLKVector2) -> Bool](./glkvector2allgreaterthanvector2%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2allgreaterthanscalar(_:_:))*