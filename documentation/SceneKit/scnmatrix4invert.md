# SCNMatrix4Invert(_:)

**Framework**: SceneKit  
**Kind**: func

Returns the inverse of the specified matrix.

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
func SCNMatrix4Invert(_ m: SCNMatrix4) -> SCNMatrix4
```

#### Return Value

The inverse matrix of the specified matrix, or the original matrix if it is not invertible.

## Parameters

- `m`: The matrix to be inverted.

## See Also

- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4translate(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](scnmatrix4rotate(_:_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4scale(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](scnmatrix4mult(_:_:).md)
  Returns the product of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4invert(_:))*