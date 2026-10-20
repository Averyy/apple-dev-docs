# SCNMatrix4Invert(_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns the inverse of the specified matrix.

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
func SCNMatrix4Invert(_ m: SCNMatrix4) -> SCNMatrix4
```

```c
extern SCNMatrix4 SCNMatrix4Invert(SCNMatrix4 m);
```

#### Return Value

The inverse matrix of the specified matrix, or the original matrix if it is not invertible.

## Parameters

- `m`: The matrix to be inverted.

## See Also

### Performing Matrix Operations
- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4translate%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4rotate%28_,_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4scale%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](./scnmatrix4mult%28_,_%29.md)
  Returns the product of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4invert(_:))*