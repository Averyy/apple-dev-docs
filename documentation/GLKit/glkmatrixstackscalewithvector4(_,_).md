# GLKMatrixStackScaleWithVector4(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a scaling operation defined by a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrixStackScaleWithVector4(_ stack: GLKMatrixStack, _ scaleVector: GLKVector4)
```

```c
void GLKMatrixStackScaleWithVector4(GLKMatrixStackRef stack, GLKVector4 scaleVector);
```

## Parameters

- `stack`: A matrix stack.
- `scaleVector`: A vector whose `x`,`y` and `z` components are used to scale the matrix.

## See Also

### Functions
- [func GLKMatrixStackCreate(CFAllocator?) -> Unmanaged<GLKMatrixStack>?](./glkmatrixstackcreate%28_%29.md)
  Allocates and returns a new matrix stack.
- [func GLKMatrixStackGetMatrix2(GLKMatrixStack) -> GLKMatrix2](./glkmatrixstackgetmatrix2%28_%29.md)
  Returns the top-left `2x2` corner of the top matrix.
- [func GLKMatrixStackGetMatrix3(GLKMatrixStack) -> GLKMatrix3](./glkmatrixstackgetmatrix3%28_%29.md)
  Returns the top-left `3x3` corner of the top matrix.
- [func GLKMatrixStackGetMatrix3Inverse(GLKMatrixStack) -> GLKMatrix3](./glkmatrixstackgetmatrix3inverse%28_%29.md)
  Fetches the top-left `3x3` corner of the top matrix and returns its inverse.
- [func GLKMatrixStackGetMatrix3InverseTranspose(GLKMatrixStack) -> GLKMatrix3](./glkmatrixstackgetmatrix3inversetranspose%28_%29.md)
  Fetches the top-left `3x3` corner of the top matrix and returns its inverse transpose.
- [func GLKMatrixStackGetMatrix4(GLKMatrixStack) -> GLKMatrix4](./glkmatrixstackgetmatrix4%28_%29.md)
  Returns a copy of the top matrix on the stack.
- [func GLKMatrixStackGetMatrix4Inverse(GLKMatrixStack) -> GLKMatrix4](./glkmatrixstackgetmatrix4inverse%28_%29.md)
  Returns the inverse of the top matrix.
- [func GLKMatrixStackGetMatrix4InverseTranspose(GLKMatrixStack) -> GLKMatrix4](./glkmatrixstackgetmatrix4inversetranspose%28_%29.md)
  Returns the inverse transpose of the top matrix.
- [func GLKMatrixStackGetTypeID() -> CFTypeID](./glkmatrixstackgettypeid%28%29.md)
  Returns the Core Foundation type for a matrix stack.
- [func GLKMatrixStackLoadMatrix4(GLKMatrixStack, GLKMatrix4)](./glkmatrixstackloadmatrix4%28_,_%29.md)
  Replaces the contents of the top matrix with a new matrix.
- [func GLKMatrixStackMultiplyMatrix4(GLKMatrixStack, GLKMatrix4)](./glkmatrixstackmultiplymatrix4%28_,_%29.md)
  Replaces the contents of the top matrix with a matrix calculated by multiplying the contents of the top matrix by another matrix.
- [func GLKMatrixStackMultiplyMatrixStack(GLKMatrixStack, GLKMatrixStack)](./glkmatrixstackmultiplymatrixstack%28_,_%29.md)
  Replaces the contents of the top matrix with a matrix calculated by multiplying the contents of the top matrix by the top matrix of another matrix stack.
- [func GLKMatrixStackPop(GLKMatrixStack)](./glkmatrixstackpop%28_%29.md)
  Removes the topmost entry from the stack.
- [func GLKMatrixStackPush(GLKMatrixStack)](./glkmatrixstackpush%28_%29.md)
  Push a copy of the topmost matrix onto the top of the stack.
- [func GLKMatrixStackRotate(GLKMatrixStack, Float, Float, Float, Float)](./glkmatrixstackrotate%28_,_,_,_,_%29.md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrixstackscalewithvector4(_:_:))*