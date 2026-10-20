# GLKVector3AllEqualToVector3(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector3AllEqualToVector3(_ vectorLeft: GLKVector3, _ vectorRight: GLKVector3) -> Bool
```

```c
static bool GLKVector3AllEqualToVector3(GLKVector3 vectorLeft, GLKVector3 vectorRight);
```

#### Return Value

[`true`](../Swift/true.md) if all of the vectors’ components are equal, [`false`](../Swift/false.md) otherwise.

## Parameters

- `vectorLeft`: The first vector.
- `vectorRight`: The second vector.

## See Also

### Comparison Operations
- [func GLKVector3AllEqualToScalar(GLKVector3, Float) -> Bool](./glkvector3allequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.
- [func GLKVector3AllGreaterThanOrEqualToScalar(GLKVector3, Float) -> Bool](./glkvector3allgreaterthanorequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector3AllGreaterThanOrEqualToVector3(GLKVector3, GLKVector3) -> Bool](./glkvector3allgreaterthanorequaltovector3%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector3AllGreaterThanScalar(GLKVector3, Float) -> Bool](./glkvector3allgreaterthanscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.
- [func GLKVector3AllGreaterThanVector3(GLKVector3, GLKVector3) -> Bool](./glkvector3allgreaterthanvector3%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector3allequaltovector3(_:_:))*