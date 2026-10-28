# GLKMatrixStackCreate(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Allocates and returns a new matrix stack.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrixStackCreate(_ alloc: CFAllocator?) -> Unmanaged<GLKMatrixStack>?
```

```c
GLKMatrixStackRefGLKMatrixStackCreate(CFAllocatorRef alloc);
```

## Return Value

A new matrix stack, or `NULL` if an error occurred.

## Discussion

A matrix stack is a Core Foundation type. Ownership follows [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

A matrix stack is initialized with a single identity matrix on the top of the stack.

## Parameters

- `alloc`: The allocator to use to allocate the matrix stack.

## See Also

### Functions
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
- [func GLKMatrixStackRotateWithVector3(GLKMatrixStack, Float, GLKVector3)](./glkmatrixstackrotatewithvector3%28_,_,_%29.md)
  Replaces the contents of the top matrix with a matrix calculated by composing the top matrix with a rotation around an arbitrary axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrixstackcreate(_:))*