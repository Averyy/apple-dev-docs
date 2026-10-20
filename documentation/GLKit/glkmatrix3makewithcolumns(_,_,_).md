# GLKMatrix3MakeWithColumns(_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a `3x3` matrix created from three column vectors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3MakeWithColumns(_ column0: GLKVector3, _ column1: GLKVector3, _ column2: GLKVector3) -> GLKMatrix3
```

```c
static GLKMatrix3 GLKMatrix3MakeWithColumns(GLKVector3 column0, GLKVector3 column1, GLKVector3 column2);
```

#### Return Value

A new matrix.

## Parameters

- `column0`: The first column.
- `column1`: The second column.
- `column2`: The third column.

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

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3makewithcolumns(_:_:_:))*