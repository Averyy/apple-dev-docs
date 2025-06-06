# GLKMatrix4MakeWithRows(_:_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a `4x4` matrix created from four row vectors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MakeWithRows(_ row0: GLKVector4, _ row1: GLKVector4, _ row2: GLKVector4, _ row3: GLKVector4) -> GLKMatrix4
```

#### Return Value

A new matrix.

## Parameters

- `row0`: The first row. The last component of the vector provides the x coordinate’s translation value.
- `row1`: The second row. The last component of the vector provides the y coordinate’s translation value.
- `row2`: The third row. The last component of the vector provides the z coordinate’s translation value.
- `row3`: The fourth row.

## See Also

- [func GLKMatrix4Make(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4make(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` matrix created from individual component values.
- [func GLKMatrix4MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeandtranspose(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` transposed matrix created from individual component values.
- [func GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharray(_:).md)
  Returns a `4x4` matrix created from an array of component values.
- [func GLKMatrix4MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharrayandtranspose(_:).md)
  Returns a `4x4` transposed matrix created from an array of component values.
- [func GLKMatrix4MakeWithColumns(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](glkmatrix4makewithcolumns(_:_:_:_:).md)
  Returns a `4x4` matrix created from four column vectors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4makewithrows(_:_:_:_:))*