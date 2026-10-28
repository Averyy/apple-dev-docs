# SCNMatrix4Rotate(_:_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a new matrix created by concatenating the specified matrix with a rotation transformation.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func SCNMatrix4Rotate(_ m: SCNMatrix4, _ angle: Float, _ x: Float, _ y: Float, _ z: Float) -> SCNMatrix4
```

*macOS*

```swift
func SCNMatrix4Rotate(_ m: SCNMatrix4, _ angle: CGFloat, _ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> SCNMatrix4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
extern SCNMatrix4 SCNMatrix4Rotate(SCNMatrix4 m, float angle, float x, float y, float z);
```

*macOS*

```c
extern SCNMatrix4 SCNMatrix4Rotate(SCNMatrix4 m, CGFloat angle, CGFloat x, CGFloat y, CGFloat z);
```

## Return Value

A new matrix.

## Discussion

The resulting transformation consists of the specified rotation followed by the transformation represented by the `mat` parameter.

## Parameters

- `m`: The matrix to be combined with a rotation.
- `angle`: The amount of rotation, in radians, measured counterclockwise around the rotation axis.
- `x`: The x-component of the rotation axis.
- `y`: The y-component of the rotation axis.
- `z`: The z-component of the rotation axis.

## See Also

### Performing Matrix Operations
- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4translate%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4scale%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](./scnmatrix4invert%28_%29.md)
  Returns the inverse of the specified matrix.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](./scnmatrix4mult%28_,_%29.md)
  Returns the product of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4rotate(_:_:_:_:_:))*