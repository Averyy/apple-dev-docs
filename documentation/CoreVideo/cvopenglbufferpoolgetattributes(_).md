# CVOpenGLBufferPoolGetAttributes(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the pool attributes dictionary for an Open GL buffer pool.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLBufferPoolGetAttributes(_ pool: CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?
```

```c
extern CFDictionaryRefCVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPoolRef pool);
```

## Return Value

The buffer-pool attributes Core Foundation dictionary, or `NULL` on failure.

## Parameters

- `pool`: The OpenGL buffer pool containing the attributes to be retrieved.

## See Also

### Functions
- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](./cvopenglbufferpoolcreate%28_,_,_,_%29.md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbufferpoolcreateopenglbuffer%28_,_,_%29.md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](./cvopenglbufferpoolgetopenglbufferattributes%28_%29.md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](./cvopenglbufferpoolgettypeid%28%29.md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.
- [CVOpenGLBufferPoolRetain](./cvopenglbufferpoolretain.md)
  Retains an OpenGL buffer pool.
- [CVOpenGLBufferPoolRelease](./cvopenglbufferpoolrelease.md)
  Releases an OpenGL buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolgetattributes(_:))*