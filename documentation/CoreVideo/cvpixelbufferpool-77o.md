# CVPixelBufferPool

**Framework**: Core Video

A utility object for managing a recyclable set of pixel buffer objects.

## Topics

### Creating pools
- [func CVPixelBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVPixelBufferPool?>) -> CVReturn](cvpixelbufferpoolcreate(_:_:_:_:).md)
  Creates a pixel buffer pool using the allocator and attributes that you specify.
- [func CVPixelBufferPoolCreatePixelBuffer(CFAllocator?, CVPixelBufferPool, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbufferpoolcreatepixelbuffer(_:_:_:).md)
  Creates a pixel buffer from a pixel buffer pool, using the allocator that you specify.
- [func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(CFAllocator?, CVPixelBufferPool, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbufferpoolcreatepixelbufferwithauxattributes(_:_:_:_:).md)
  Creates a new pixel buffer with auxiliary attributes from the pool.
### Flushing pools
- [func CVPixelBufferPoolFlush(CVPixelBufferPool, CVPixelBufferPoolFlushFlags)](cvpixelbufferpoolflush(_:_:).md)
  Frees pixel buffers from the pool based on the options that you specify.
### Inspecting pools
- [func CVPixelBufferPoolGetAttributes(CVPixelBufferPool) -> CFDictionary?](cvpixelbufferpoolgetattributes(_:).md)
  The pool attributes dictionary for a pixel buffer pool.
- [func CVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPool) -> CFDictionary?](cvpixelbufferpoolgetpixelbufferattributes(_:).md)
  The attributes of pixel buffers which the system creates using the pool you specify.
- [func CVPixelBufferPoolGetTypeID() -> CFTypeID](cvpixelbufferpoolgettypeid().md)
  Returns the Core Foundation type identifier of the pixel buffer pool type.
### Data types
- [class CVPixelBufferPool](cvpixelbufferpool.md)
  A reference to a pixel buffer pool object.
- [struct CVPixelBufferPoolFlushFlags](cvpixelbufferpoolflushflags.md)
  The flags to pass to flush the pool.
### Constants
- [let kCVPixelBufferPoolMinimumBufferCountKey: CFString](kcvpixelbufferpoolminimumbuffercountkey.md)
  The minimum number of buffers allowed in the pixel buffer pool.
- [let kCVPixelBufferPoolMaximumBufferAgeKey: CFString](kcvpixelbufferpoolmaximumbufferagekey.md)
  The key you use to set the maximum allowable age for a buffer in the pixel buffer pool.
- [let kCVPixelBufferPoolAllocationThresholdKey: CFString](kcvpixelbufferpoolallocationthresholdkey.md)
  The key you use to set the auxiliary attributes dictionary.
### Notifications
- [let kCVPixelBufferPoolFreeBufferNotification: CFString](kcvpixelbufferpoolfreebuffernotification.md)
  A notification that the system posts if a buffer becomes available after it fails to create a pixel buffer with auxiliary attributes because it exceeded the threshold you specified.

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [CVBuffer](cvbuffer-nfm.md)
  An abstract base class that defines how to interact with data buffers.
- [CVImageBuffer](cvimagebuffer-q40.md)
  An interface for managing different types of image data.
- [CVPixelBuffer](cvpixelbuffer-q2e.md)
  An image buffer that holds pixels in main memory.
- [CVPixelFormatDescription](cvpixelformatdescription.md)
  An API that provides functions and types for defining custom pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpool-77o)*