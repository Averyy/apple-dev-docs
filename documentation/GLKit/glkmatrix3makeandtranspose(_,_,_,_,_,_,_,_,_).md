# GLKMatrix3MakeAndTranspose(_:_:_:_:_:_:_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a `3x3` transposed matrix created from individual component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3MakeAndTranspose(_ m00: Float, _ m01: Float, _ m02: Float, _ m10: Float, _ m11: Float, _ m12: Float, _ m20: Float, _ m21: Float, _ m22: Float) -> GLKMatrix3
```

```c
static GLKMatrix3 GLKMatrix3MakeAndTranspose(float m00, float m01, float m02, float m10, float m11, float m12, float m20, float m21, float m22);
```

## Return Value

A new matrix.

## Parameters

- `m00`: The value for position [0,0] in the returned matrix.
- `m01`: The value for position [1,0] in the returned matrix.
- `m02`: The value for position [2,0] in the returned matrix.
- `m10`: The value for position [0,1] in the returned matrix.
- `m11`: The value for position [1,1] in the returned matrix.
- `m12`: The value for position [2,1] in the returned matrix.
- `m20`: The value for position [0,2] in the returned matrix.
- `m21`: The value for position [1,2] in the returned matrix.
- `m22`: The value for position [2,2] in the returned matrix.

## See Also

### Creating Matrices
- [func GLKMatrix3Make(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3](./glkmatrix3make%28_,_,_,_,_,_,_,_,_%29.md)
  Returns a `3x3` matrix created from individual component values.
- [func GLKMatrix3MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix3](./glkmatrix3makewitharray%28_%29.md)
  Returns a `3x3` matrix created from an array of component values.
- [func GLKMatrix3MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix3](./glkmatrix3makewitharrayandtranspose%28_%29.md)
  Returns a `3x3` transposed matrix created from an array of component values.
- [func GLKMatrix3MakeWithColumns(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3](./glkmatrix3makewithcolumns%28_,_,_%29.md)
  Returns a `3x3` matrix created from three column vectors.
- [func GLKMatrix3MakeWithRows(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3](./glkmatrix3makewithrows%28_,_,_%29.md)
  Returns a `3x3` matrix created from three row vectors.
- [func GLKMatrix3MakeRotation(Float, Float, Float, Float) -> GLKMatrix3](./glkmatrix3makerotation%28_,_,_,_%29.md)
  Returns a `3x3` matrix that performs a rotation around an arbitrary vector.
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

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3makeandtranspose(_:_:_:_:_:_:_:_:_:))*