# SCNMatrix4IsIdentity(_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the specified matrix is equal to the identity matrix.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func SCNMatrix4IsIdentity(_ m: SCNMatrix4) -> Bool
```

```c
extern bool SCNMatrix4IsIdentity(SCNMatrix4 m);
```

## Return Value

True if the elements on the matrix’s diagonal are `1.0` and all other elements are `0.0`.

## Parameters

- `m`: The matrix to be tested.

## See Also

### Related Documentation
- [let SCNMatrix4Identity: SCNMatrix4](./scnmatrix4identity.md)
  The 4 x 4 identity matrix.
### Comparing Matrices
- [func SCNMatrix4EqualToMatrix4(SCNMatrix4, SCNMatrix4) -> Bool](./scnmatrix4equaltomatrix4%28_,_%29.md)
  Returns a Boolean value that indicates whether the corresponding elements of two matrices are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4isidentity(_:))*