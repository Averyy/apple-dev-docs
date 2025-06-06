# GLKit Functions

**Framework**: GLKit

## Topics

### Functions
- [func GLKMatrixStackCreate(CFAllocator?) -> Unmanaged<GLKMatrixStack>?](glkmatrixstackcreate(_:).md)
  Allocates and returns a new matrix stack.
- [func GLKMatrixStackGetMatrix2(GLKMatrixStack) -> GLKMatrix2](glkmatrixstackgetmatrix2(_:).md)
  Returns the top-left `2x2` corner of the top matrix.
- [func GLKMatrixStackGetMatrix3(GLKMatrixStack) -> GLKMatrix3](glkmatrixstackgetmatrix3(_:).md)
  Returns the top-left `3x3` corner of the top matrix.
- [func GLKMatrixStackGetMatrix3Inverse(GLKMatrixStack) -> GLKMatrix3](glkmatrixstackgetmatrix3inverse(_:).md)
  Fetches the top-left `3x3` corner of the top matrix and returns its inverse.
- [func GLKMatrixStackGetMatrix3InverseTranspose(GLKMatrixStack) -> GLKMatrix3](glkmatrixstackgetmatrix3inversetranspose(_:).md)
  Fetches the top-left `3x3` corner of the top matrix and returns its inverse transpose.
- [func GLKMatrixStackGetMatrix4(GLKMatrixStack) -> GLKMatrix4](glkmatrixstackgetmatrix4(_:).md)
  Returns a copy of the top matrix on the stack.
- [func GLKMatrixStackGetMatrix4Inverse(GLKMatrixStack) -> GLKMatrix4](glkmatrixstackgetmatrix4inverse(_:).md)
  Returns the inverse of the top matrix.
- [func GLKMatrixStackGetMatrix4InverseTranspose(GLKMatrixStack) -> GLKMatrix4](glkmatrixstackgetmatrix4inversetranspose(_:).md)
  Returns the inverse transpose of the top matrix.
- [func GLKMatrixStackGetTypeID() -> CFTypeID](glkmatrixstackgettypeid().md)
  Returns the Core Foundation type for a matrix stack.
- [func GLKMatrixStackLoadMatrix4(GLKMatrixStack, GLKMatrix4)](glkmatrixstackloadmatrix4(_:_:).md)
  Replaces the contents of the top matrix with a new matrix.
- [func GLKMatrixStackMultiplyMatrix4(GLKMatrixStack, GLKMatrix4)](glkmatrixstackmultiplymatrix4(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by multiplying the contents of the top matrix by another matrix.
- [func GLKMatrixStackMultiplyMatrixStack(GLKMatrixStack, GLKMatrixStack)](glkmatrixstackmultiplymatrixstack(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by multiplying the contents of the top matrix by the top matrix of another matrix stack.
- [func GLKMatrixStackPop(GLKMatrixStack)](glkmatrixstackpop(_:).md)
  Removes the topmost entry from the stack.
- [func GLKMatrixStackPush(GLKMatrixStack)](glkmatrixstackpush(_:).md)
  Push a copy of the topmost matrix onto the top of the stack.
- [func GLKMatrixStackRotate(GLKMatrixStack, Float, Float, Float, Float)](glkmatrixstackrotate(_:_:_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.
- [func GLKMatrixStackRotateWithVector3(GLKMatrixStack, Float, GLKVector3)](glkmatrixstackrotatewithvector3(_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.
- [func GLKMatrixStackRotateWithVector4(GLKMatrixStack, Float, GLKVector4)](glkmatrixstackrotatewithvector4(_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.
- [func GLKMatrixStackRotateX(GLKMatrixStack, Float)](glkmatrixstackrotatex(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around the positive-x axis.
- [func GLKMatrixStackRotateY(GLKMatrixStack, Float)](glkmatrixstackrotatey(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around the positive-y axis.
- [func GLKMatrixStackRotateZ(GLKMatrixStack, Float)](glkmatrixstackrotatez(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around the positive-z axis.
- [func GLKMatrixStackScale(GLKMatrixStack, Float, Float, Float)](glkmatrixstackscale(_:_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by scaling the contents of the top matrix.
- [func GLKMatrixStackScaleWithVector3(GLKMatrixStack, GLKVector3)](glkmatrixstackscalewithvector3(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a scaling operation.
- [func GLKMatrixStackScaleWithVector4(GLKMatrixStack, GLKVector4)](glkmatrixstackscalewithvector4(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a scaling operation defined by a vector.
- [func GLKMatrixStackSize(GLKMatrixStack) -> Int32](glkmatrixstacksize(_:).md)
  Returns the number of matrices present on the matrix stack.
- [func GLKMatrixStackTranslate(GLKMatrixStack, Float, Float, Float)](glkmatrixstacktranslate(_:_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a translation operation.
- [func GLKMatrixStackTranslateWithVector3(GLKMatrixStack, GLKVector3)](glkmatrixstacktranslatewithvector3(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a translation defined by a vector.
- [func GLKMatrixStackTranslateWithVector4(GLKMatrixStack, GLKVector4)](glkmatrixstacktranslatewithvector4(_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a translation defined by a vector.
- [func GLKVertexAttributeParametersFromModelIO(MDLVertexFormat) -> GLKVertexAttributeParameters](glkvertexattributeparametersfrommodelio(_:).md)

## See Also

- [GLKit Structures](glkit-structures.md)
- [GLKit Enumerations](glkit-enumerations.md)
- [GLKit Constants](glkit-constants.md)
- [GLKit Data Types](glkit-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkit-functions)*