# GLKMatrix4MakeWithColumns(_:_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a `4x4` matrix created from four column vectors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MakeWithColumns(_ column0: GLKVector4, _ column1: GLKVector4, _ column2: GLKVector4, _ column3: GLKVector4) -> GLKMatrix4
```

```c
static GLKMatrix4 GLKMatrix4MakeWithColumns(GLKVector4 column0, GLKVector4 column1, GLKVector4 column2, GLKVector4 column3);
```

## Return Value

A new matrix.

## Discussion

The first three components of the `column3` parameter provide the translation values for the matrix.

## Parameters

- `column0`: The first column.
- `column1`: The second column.
- `column2`: The third column.
- `column3`: The four column.

## See Also

### Creating Matrices
- [func GLKMatrix4Make(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4make%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Returns a `4x4` matrix created from individual component values.
- [func GLKMatrix4MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4makeandtranspose%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Returns a `4x4` transposed matrix created from individual component values.
- [func GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix4](./glkmatrix4makewitharray%28_%29.md)
  Returns a `4x4` matrix created from an array of component values.
- [func GLKMatrix4MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix4](./glkmatrix4makewitharrayandtranspose%28_%29.md)
  Returns a `4x4` transposed matrix created from an array of component values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4makewithcolumns(_:_:_:_:))*