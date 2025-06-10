# SCNMatrix4Rotate(_:_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a new matrix created by concatenating the specified matrix with a rotation transformation.

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
func SCNMatrix4Rotate(_ m: SCNMatrix4, _ angle: CGFloat, _ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> SCNMatrix4
```

#### Return Value

A new matrix.

#### Discussion

The resulting transformation consists of the specified rotation followed by the transformation represented by the `mat` parameter.

## Parameters

- `m`: The matrix to be combined with a rotation.
- `angle`: The amount of rotation, in radians, measured counterclockwise around the rotation axis.
- `x`: The x-component of the rotation axis.
- `y`: The y-component of the rotation axis.
- `z`: The z-component of the rotation axis.

## See Also

- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4translate(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4scale(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](scnmatrix4invert(_:).md)
  Returns the inverse of the specified matrix.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](scnmatrix4mult(_:_:).md)
  Returns the product of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4rotate(_:_:_:_:_:))*