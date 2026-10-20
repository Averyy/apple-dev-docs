# GLKVector2AllGreaterThanVector2(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector2AllGreaterThanVector2(_ vectorLeft: GLKVector2, _ vectorRight: GLKVector2) -> Bool
```

```c
static bool GLKVector2AllGreaterThanVector2(GLKVector2 vectorLeft, GLKVector2 vectorRight);
```

#### Return Value

[`true`](../Swift/true.md) if each component in the first vector is greater than the corresponding component of the second vector, [`false`](../Swift/false.md) otherwise.

## Parameters

- `vectorLeft`: The first vector.
- `vectorRight`: The second vector.

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
- [func GLKVector2AllGreaterThanScalar(GLKVector2, Float) -> Bool](./glkvector2allgreaterthanscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2allgreaterthanvector2(_:_:))*