# GLKMatrix4MakeFrustum(_:_:_:_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a `4x4` perspective projection matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MakeFrustum(_ left: Float, _ right: Float, _ bottom: Float, _ top: Float, _ nearZ: Float, _ farZ: Float) -> GLKMatrix4
```

#### Return Value

A projection matrix.

#### Discussion

This function creates the same orthographic projection matrix previously provided in OpenGL ES 1.1 by the `glFrustum` function.

## Parameters

- `left`: The left clipping plane.
- `right`: The right clipping plane.
- `bottom`: The bottom clipping plane.
- `top`: The top clipping plane.
- `nearZ`: The near clipping distance. Must be positive.
- `farZ`: The far clipping distance.  Must be positive and greater than the near distance.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4makefrustum(_:_:_:_:_:_:))*