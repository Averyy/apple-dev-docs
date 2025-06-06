# GLKMatrixStackPop(_:)

**Framework**: GLKit  
**Kind**: func

Removes the topmost entry from the stack.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrixStackPop(_ stack: GLKMatrixStack)
```

#### Discussion

This function does nothing if the stack is already empty.

## Parameters

- `stack`: A matrix stack.

## See Also

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
- [func GLKMatrixStackPush(GLKMatrixStack)](glkmatrixstackpush(_:).md)
  Push a copy of the topmost matrix onto the top of the stack.
- [func GLKMatrixStackRotate(GLKMatrixStack, Float, Float, Float, Float)](glkmatrixstackrotate(_:_:_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.
- [func GLKMatrixStackRotateWithVector3(GLKMatrixStack, Float, GLKVector3)](glkmatrixstackrotatewithvector3(_:_:_:).md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrixstackpop(_:))*