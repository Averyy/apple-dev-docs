# GLKMatrix4Make(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a `4x4` matrix created from individual component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4Make(_ m00: Float, _ m01: Float, _ m02: Float, _ m03: Float, _ m10: Float, _ m11: Float, _ m12: Float, _ m13: Float, _ m20: Float, _ m21: Float, _ m22: Float, _ m23: Float, _ m30: Float, _ m31: Float, _ m32: Float, _ m33: Float) -> GLKMatrix4
```

```c
static GLKMatrix4 GLKMatrix4Make(float m00, float m01, float m02, float m03, float m10, float m11, float m12, float m13, float m20, float m21, float m22, float m23, float m30, float m31, float m32, float m33);
```

#### Return Value

A new matrix.

#### Discussion

The values in `m30`, `m31`, and `m32` correspond to the translation values `tx`, `ty`, and `tz`, respectively.

## Parameters

- `m00`: The value for position [0,0] in the returned matrix.
- `m01`: The value for position [0,1] in the returned matrix.
- `m02`: The value for position [0,2] in the returned matrix.
- `m03`: The value for position [0,3] in the returned matrix.
- `m10`: The value for position [1,0] in the returned matrix.
- `m11`: The value for position [1,1] in the returned matrix.
- `m12`: The value for position [1,2] in the returned matrix.
- `m13`: The value for position [1,3] in the returned matrix.
- `m20`: The value for position [2,0] in the returned matrix.
- `m21`: The value for position [2,1] in the returned matrix.
- `m22`: The value for position [2,2] in the returned matrix.
- `m23`: The value at position [2,3] in the returned matrix.
- `m30`: The value for position [3,0] in the returned matrix.
- `m31`: The value for position [3,1] in the returned matrix.
- `m32`: The value for position [3,2] in the returned matrix.
- `m33`: The value for position [3,3] in the returned matrix.

## See Also

### Creating Matrices
- [func GLKMatrix4MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4makeandtranspose%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Returns a `4x4` transposed matrix created from individual component values.
- [func GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix4](./glkmatrix4makewitharray%28_%29.md)
  Returns a `4x4` matrix created from an array of component values.
- [func GLKMatrix4MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix4](./glkmatrix4makewitharrayandtranspose%28_%29.md)
  Returns a `4x4` transposed matrix created from an array of component values.
- [func GLKMatrix4MakeWithColumns(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](./glkmatrix4makewithcolumns%28_,_,_,_%29.md)
  Returns a `4x4` matrix created from four column vectors.
- [func GLKMatrix4MakeWithRows(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](./glkmatrix4makewithrows%28_,_,_,_%29.md)
  Returns a `4x4` matrix created from four row vectors.
- [func GLKMatrix4MakeRotation(Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4makerotation%28_,_,_,_%29.md)
  Returns a `4x4` matrix that performs a rotation around an arbitrary vector.
- [func GLKMatrix4MakeXRotation(Float) -> GLKMatrix4](./glkmatrix4makexrotation%28_%29.md)
  Returns a `4x4` matrix that performs a rotation around the positive x-axis.
- [func GLKMatrix4MakeYRotation(Float) -> GLKMatrix4](./glkmatrix4makeyrotation%28_%29.md)
  Returns a `4x4` matrix that performs a rotation around the positive y-axis.
- [func GLKMatrix4MakeZRotation(Float) -> GLKMatrix4](./glkmatrix4makezrotation%28_%29.md)
  Returns a `4x4` matrix that performs a rotation around the positive z-axis.
- [func GLKMatrix4MakeWithQuaternion(GLKQuaternion) -> GLKMatrix4](./glkmatrix4makewithquaternion%28_%29.md)
  Returns a `4x4` matrix that performs a rotation based on a quaternion.
- [func GLKMatrix4MakeScale(Float, Float, Float) -> GLKMatrix4](./glkmatrix4makescale%28_,_,_%29.md)
  Returns a `4x4` matrix that performs a scaling transformation.
- [func GLKMatrix4MakeTranslation(Float, Float, Float) -> GLKMatrix4](./glkmatrix4maketranslation%28_,_,_%29.md)
  Returns a `4x4` matrix that performs a translation.
- [func GLKMatrix4MakeLookAt(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4makelookat%28_,_,_,_,_,_,_,_,_%29.md)
  Returns a `4x4` matrix that transforms world coordinates to eye coordinates.
- [func GLKMatrix4MakeOrtho(Float, Float, Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4makeortho%28_,_,_,_,_,_%29.md)
  Returns a `4x4` orthographic projection matrix.
- [func GLKMatrix4MakePerspective(Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4makeperspective%28_,_,_,_%29.md)
  Returns a `4x4` perspective projection matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4make(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*