# SCNMatrix4IsIdentity(_:)

**Framework**: SceneKit  
**Kind**: func

Returns a Boolean value that indicates whether the specified matrix is equal to the identity matrix.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SCNMatrix4IsIdentity(_ m: SCNMatrix4) -> Bool
```

#### Return Value

True if the elements on the matrix’s diagonal are `1.0` and all other elements are `0.0`.

## Parameters

- `m`: The matrix to be tested.

## See Also

- [let SCNMatrix4Identity: SCNMatrix4](scnmatrix4identity.md)
  The 4 x 4 identity matrix.
- [func SCNMatrix4EqualToMatrix4(SCNMatrix4, SCNMatrix4) -> Bool](scnmatrix4equaltomatrix4(_:_:).md)
  Returns a Boolean value that indicates whether the corresponding elements of two matrices are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4isidentity(_:))*