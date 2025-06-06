# GLKMatrix4MakeWithArrayAndTranspose(_:)

**Framework**: GLKit  
**Kind**: func

Returns a `4x4` transposed matrix created from an array of component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MakeWithArrayAndTranspose(_ values: UnsafeMutablePointer<Float>!) -> GLKMatrix4
```

#### Return Value

A new matrix.

#### Discussion

The matrix is created and then transposed, before being returned to your application.

The values at indices `3`, `7`, and `11` correspond to the translation values `tx`, `ty`, and `tz`, respectively.

## Parameters

- `values`: An array of component values, in column-major order.

## See Also

- [func GLKMatrix4Make(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4make(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` matrix created from individual component values.
- [func GLKMatrix4MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeandtranspose(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` transposed matrix created from individual component values.
- [func GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharray(_:).md)
  Returns a `4x4` matrix created from an array of component values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4makewitharrayandtranspose(_:))*