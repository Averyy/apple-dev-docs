# GLKMatrix4MakeAndTranspose(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a `4x4` transposed matrix created from individual component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MakeAndTranspose(_ m00: Float, _ m01: Float, _ m02: Float, _ m03: Float, _ m10: Float, _ m11: Float, _ m12: Float, _ m13: Float, _ m20: Float, _ m21: Float, _ m22: Float, _ m23: Float, _ m30: Float, _ m31: Float, _ m32: Float, _ m33: Float) -> GLKMatrix4
```

#### Return Value

A new matrix.

#### Discussion

The values in `m03`, `m13`, and `m23` correspond to the translation values `tx`, `ty`, and `tz`, respectively.

## Parameters

- `m00`: The value for position [0,0] in the returned matrix.
- `m01`: The value for position [1,0] in the returned matrix.
- `m02`: The value for position [2,0] in the returned matrix.
- `m03`: The value for position [3,0] in the returned matrix.
- `m10`: The value for position [0,1] in the returned matrix.
- `m11`: The value for position [1,1] in the returned matrix.
- `m12`: The value for position [2,1] in the returned matrix.
- `m13`: The value for position [3,1] in the returned matrix.
- `m20`: The value for position [0,2] in the returned matrix.
- `m21`: The value for position [1,2] in the returned matrix.
- `m22`: The value for position [2,2] in the returned matrix.
- `m23`: The value for position [3,2] in the returned matrix.
- `m30`: The value for position [0,3] in the returned matrix.
- `m31`: The value for position [1,3] in the returned matrix.
- `m32`: The value for position [2,3] in the returned matrix.
- `m33`: The value for position [3,3] in the returned matrix.

## See Also

- [func GLKMatrix4Make(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4make(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` matrix created from individual component values.
- [func GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharray(_:).md)
  Returns a `4x4` matrix created from an array of component values.
- [func GLKMatrix4MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharrayandtranspose(_:).md)
  Returns a `4x4` transposed matrix created from an array of component values.
- [func GLKMatrix4MakeWithColumns(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](glkmatrix4makewithcolumns(_:_:_:_:).md)
  Returns a `4x4` matrix created from four column vectors.
- [func GLKMatrix4MakeWithRows(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](glkmatrix4makewithrows(_:_:_:_:).md)
  Returns a `4x4` matrix created from four row vectors.
- [func GLKMatrix4MakeRotation(Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makerotation(_:_:_:_:).md)
  Returns a `4x4` matrix that performs a rotation around an arbitrary vector.
- [func GLKMatrix4MakeXRotation(Float) -> GLKMatrix4](glkmatrix4makexrotation(_:).md)
  Returns a `4x4` matrix that performs a rotation around the positive x-axis.
- [func GLKMatrix4MakeYRotation(Float) -> GLKMatrix4](glkmatrix4makeyrotation(_:).md)
  Returns a `4x4` matrix that performs a rotation around the positive y-axis.
- [func GLKMatrix4MakeZRotation(Float) -> GLKMatrix4](glkmatrix4makezrotation(_:).md)
  Returns a `4x4` matrix that performs a rotation around the positive z-axis.
- [func GLKMatrix4MakeWithQuaternion(GLKQuaternion) -> GLKMatrix4](glkmatrix4makewithquaternion(_:).md)
  Returns a `4x4` matrix that performs a rotation based on a quaternion.
- [func GLKMatrix4MakeScale(Float, Float, Float) -> GLKMatrix4](glkmatrix4makescale(_:_:_:).md)
  Returns a `4x4` matrix that performs a scaling transformation.
- [func GLKMatrix4MakeTranslation(Float, Float, Float) -> GLKMatrix4](glkmatrix4maketranslation(_:_:_:).md)
  Returns a `4x4` matrix that performs a translation.
- [func GLKMatrix4MakeLookAt(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makelookat(_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` matrix that transforms world coordinates to eye coordinates.
- [func GLKMatrix4MakeOrtho(Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeortho(_:_:_:_:_:_:).md)
  Returns a `4x4` orthographic projection matrix.
- [func GLKMatrix4MakePerspective(Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeperspective(_:_:_:_:).md)
  Returns a `4x4` perspective projection matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4makeandtranspose(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*