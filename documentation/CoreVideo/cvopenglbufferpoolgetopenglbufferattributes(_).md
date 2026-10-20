# CVOpenGLBufferPoolGetOpenGLBufferAttributes(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the attributes of OpenGL buffers that will be created from a buffer pool.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLBufferPoolGetOpenGLBufferAttributes(_ pool: CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?
```

```c
extern CFDictionaryRefCVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPoolRef pool);
```

#### Return Value

The OpenGL buffer attributes Core Foundation dictionary, or `NULL` on failure.

#### Discussion

You can use this function to obtain information about the OpenGL buffers that will be created from the buffer pool.

## Parameters

- `pool`: The OpenGL buffer pool containing the attributes to be retrieved.

## See Also

### Functions
- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](./cvopenglbufferpoolcreate%28_,_,_,_%29.md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbufferpoolcreateopenglbuffer%28_,_,_%29.md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](./cvopenglbufferpoolgetattributes%28_%29.md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](./cvopenglbufferpoolgettypeid%28%29.md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolgetopenglbufferattributes(_:))*