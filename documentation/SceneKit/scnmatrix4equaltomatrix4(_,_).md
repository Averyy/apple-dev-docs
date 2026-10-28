# SCNMatrix4EqualToMatrix4(_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the corresponding elements of two matrices are equal.

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
func SCNMatrix4EqualToMatrix4(_ a: SCNMatrix4, _ b: SCNMatrix4) -> Bool
```

```c
extern bool SCNMatrix4EqualToMatrix4(SCNMatrix4 a, SCNMatrix4 b);
```

## Return Value

True if each element in `matA` is exactly equal to the corresponding element in `b`.

## Discussion

This function performs a numeric (not bitwise) comparison of each pair of elements.

## Parameters

- `a`: The first matrix to be compared.
- `b`: The first matrix to be compared.

## See Also

### Comparing Matrices
- [func SCNMatrix4IsIdentity(SCNMatrix4) -> Bool](./scnmatrix4isidentity%28_%29.md)
  Returns a Boolean value that indicates whether the specified matrix is equal to the identity matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4equaltomatrix4(_:_:))*