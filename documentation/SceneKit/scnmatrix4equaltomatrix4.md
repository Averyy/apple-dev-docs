# SCNMatrix4EqualToMatrix4(_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a Boolean value that indicates whether the corresponding elements of two matrices are equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func SCNMatrix4EqualToMatrix4(_ a: SCNMatrix4, _ b: SCNMatrix4) -> Bool
```

#### Return Value

True if each element in `matA` is exactly equal to the corresponding element in `b`.

#### Discussion

This function performs a numeric (not bitwise) comparison of each pair of elements.

## Parameters

- `a`: The first matrix to be compared.
- `b`: The first matrix to be compared.

## See Also

- [func SCNMatrix4IsIdentity(SCNMatrix4) -> Bool](scnmatrix4isidentity(_:).md)
  Returns a Boolean value that indicates whether the specified matrix is equal to the identity matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4equaltomatrix4(_:_:))*