# CVOpenGLBufferPoolRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases an OpenGL buffer pool.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```c
extern void CVOpenGLBufferPoolRelease(CVOpenGLBufferPoolRef openGLBufferPool);
```

## Discussion

This function is equivalent to `CFRelease`, but is `NULL` safe.

## Parameters

- `openGLBufferPool`: The OpenGL buffer pool that you want to release.

## See Also

### Functions
- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](./cvopenglbufferpoolcreate%28_,_,_,_%29.md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbufferpoolcreateopenglbuffer%28_,_,_%29.md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](./cvopenglbufferpoolgetattributes%28_%29.md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](./cvopenglbufferpoolgetopenglbufferattributes%28_%29.md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](./cvopenglbufferpoolgettypeid%28%29.md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.
- [CVOpenGLBufferPoolRetain](./cvopenglbufferpoolretain.md)
  Retains an OpenGL buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolrelease)*