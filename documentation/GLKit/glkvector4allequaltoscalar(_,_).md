# GLKVector4AllEqualToScalar(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector4AllEqualToScalar(_ vector: GLKVector4, _ value: Float) -> Bool
```

```c
static bool GLKVector4AllEqualToScalar(GLKVector4 vector, float value);
```

## Return Value

[`true`](../Swift/true.md) if all of the vector’s components are equal to `value`, [`false`](../Swift/false.md) otherwise.

## Parameters

- `vector`: A vector.
- `value`: A scalar.

## See Also

### Comparison Operations
- [func GLKVector4AllEqualToVector4(GLKVector4, GLKVector4) -> Bool](./glkvector4allequaltovector4%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.
- [func GLKVector4AllGreaterThanOrEqualToScalar(GLKVector4, Float) -> Bool](./glkvector4allgreaterthanorequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector4AllGreaterThanOrEqualToVector4(GLKVector4, GLKVector4) -> Bool](./glkvector4allgreaterthanorequaltovector4%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector4AllGreaterThanScalar(GLKVector4, Float) -> Bool](./glkvector4allgreaterthanscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.
- [func GLKVector4AllGreaterThanVector4(GLKVector4, GLKVector4) -> Bool](./glkvector4allgreaterthanvector4%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4allequaltoscalar(_:_:))*