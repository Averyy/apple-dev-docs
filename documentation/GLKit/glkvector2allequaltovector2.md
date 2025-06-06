# GLKVector2AllEqualToVector2(_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector2AllEqualToVector2(_ vectorLeft: GLKVector2, _ vectorRight: GLKVector2) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if all of the vectors’ components are equal , [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The vectors are considered equal when the value for the component at each position in the two source vectors is equal.

## Parameters

- `vectorLeft`: The first vector.
- `vectorRight`: The second vector.

## See Also

- [func GLKVector2AllEqualToScalar(GLKVector2, Float) -> Bool](glkvector2allequaltoscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.
- [func GLKVector2AllGreaterThanOrEqualToScalar(GLKVector2, Float) -> Bool](glkvector2allgreaterthanorequaltoscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector2AllGreaterThanOrEqualToVector2(GLKVector2, GLKVector2) -> Bool](glkvector2allgreaterthanorequaltovector2(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector2AllGreaterThanScalar(GLKVector2, Float) -> Bool](glkvector2allgreaterthanscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.
- [func GLKVector2AllGreaterThanVector2(GLKVector2, GLKVector2) -> Bool](glkvector2allgreaterthanvector2(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2allequaltovector2(_:_:))*