# CVOpenGLBufferPoolCreate(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Creates a new OpenGL buffer pool.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLBufferPoolCreate(_ allocator: CFAllocator?, _ poolAttributes: CFDictionary?, _ openGLBufferAttributes: CFDictionary?, _ poolOut: UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn
```

```c
extern CVReturn CVOpenGLBufferPoolCreate(CFAllocatorRef allocator, CFDictionaryRef poolAttributes, CFDictionaryRef openGLBufferAttributes, CVOpenGLBufferPoolRef*poolOut);
```

## Return Value

A Core Video result code. See[Core Video Constants](./core-video-constants.md) for possible values.

## Parameters

- `allocator`: The allocator to use for allocating this buffer pool. Pass `NULL` to specify the default allocator.
- `poolAttributes`: A Core Foundation dictionary containing the attributes to be used for the pool itself.
- `openGLBufferAttributes`: A Core Foundation dictionary containing the attributes to be used for creating new OpenGL buffers within the pool.
- `poolOut`: On output, `poolOut` points to the new OpenGL buffer pool.

## See Also

### Functions
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
- [CVOpenGLBufferPoolRelease](./cvopenglbufferpoolrelease.md)
  Releases an OpenGL buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolcreate(_:_:_:_:))*