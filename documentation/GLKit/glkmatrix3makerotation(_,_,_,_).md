# GLKMatrix3MakeRotation(_:_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a `3x3` matrix that performs a rotation around an arbitrary vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3MakeRotation(_ radians: Float, _ x: Float, _ y: Float, _ z: Float) -> GLKMatrix3
```

```c
static GLKMatrix3 GLKMatrix3MakeRotation(float radians, float x, float y, float z);
```

#### Return Value

A new rotation matrix.

## Parameters

- `radians`: The angle of the rotation (a positive angle is counterclockwise).
- `x`: The `x` component of the rotation vector.
- `y`: The `y` component of the rotation vector.
- `z`: The `z` component of the rotation vector.

## See Also

### Creating Matrices
- [func GLKMatrix3Make(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3](./glkmatrix3make%28_,_,_,_,_,_,_,_,_%29.md)
  Returns a `3x3` matrix created from individual component values.
- [func GLKMatrix3MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3](./glkmatrix3makeandtranspose%28_,_,_,_,_,_,_,_,_%29.md)
  Returns a `3x3` transposed matrix created from individual component values.
- [func GLKMatrix3MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix3](./glkmatrix3makewitharray%28_%29.md)
  Returns a `3x3` matrix created from an array of component values.
- [func GLKMatrix3MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix3](./glkmatrix3makewitharrayandtranspose%28_%29.md)
  Returns a `3x3` transposed matrix created from an array of component values.
- [func GLKMatrix3MakeWithColumns(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3](./glkmatrix3makewithcolumns%28_,_,_%29.md)
  Returns a `3x3` matrix created from three column vectors.
- [func GLKMatrix3MakeWithRows(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3](./glkmatrix3makewithrows%28_,_,_%29.md)
  Returns a `3x3` matrix created from three row vectors.
- [func GLKMatrix3MakeXRotation(Float) -> GLKMatrix3](./glkmatrix3makexrotation%28_%29.md)
  Returns a `3x3` matrix that performs a rotation around the positive x-axis.
- [func GLKMatrix3MakeYRotation(Float) -> GLKMatrix3](./glkmatrix3makeyrotation%28_%29.md)
  Returns a `3x3` matrix that performs a rotation around the positive y-axis.
- [func GLKMatrix3MakeZRotation(Float) -> GLKMatrix3](./glkmatrix3makezrotation%28_%29.md)
  Returns a `3x3` matrix that performs a rotation around the positive z-axis.
- [func GLKMatrix3MakeWithQuaternion(GLKQuaternion) -> GLKMatrix3](./glkmatrix3makewithquaternion%28_%29.md)
  Returns a `3x3` matrix that performs a rotation based on a quaternion.
- [func GLKMatrix3MakeScale(Float, Float, Float) -> GLKMatrix3](./glkmatrix3makescale%28_,_,_%29.md)
  Returns a `3x3` matrix that performs a scaling transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3makerotation(_:_:_:_:))*