# CVPixelBuffer

**Framework**: Core Video

An image buffer that holds pixels in main memory.

#### Overview

A Core Video pixel buffer is an image buffer that holds pixels in main memory. Applications generating frames, compressing or decompressing video, or using Core Image can all make use of Core Video pixel buffers.

## Topics

### Creating pixel buffers
- [func CVPixelBufferCreate(CFAllocator?, Int, Int, OSType, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreate(_:_:_:_:_:_:).md)
  Creates a single pixel buffer for a given size and pixel format.
- [func CVPixelBufferCreateWithBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer, Int, CVPixelBufferReleaseBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:).md)
  Creates a pixel buffer for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithPlanarBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a single pixel buffer in planar format for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithIOSurface(CFAllocator?, IOSurfaceRef, CFDictionary?, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn](cvpixelbuffercreatewithiosurface(_:_:_:_:).md)
  Creates a single pixel buffer for the IO surface that you specify.
### Inspecting Pixel Buffers
- [func CVPixelBufferGetBaseAddress(CVPixelBuffer) -> UnsafeMutableRawPointer?](cvpixelbuffergetbaseaddress(_:).md)
  Returns the base address of the pixel buffer.
- [func CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer, Int) -> UnsafeMutableRawPointer?](cvpixelbuffergetbaseaddressofplane(_:_:).md)
  Returns the base address of the plane at the specified plane index.
- [func CVPixelBufferGetBytesPerRow(CVPixelBuffer) -> Int](cvpixelbuffergetbytesperrow(_:).md)
  Returns the number of bytes per row of the pixel buffer.
- [func CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer, Int) -> Int](cvpixelbuffergetbytesperrowofplane(_:_:).md)
  Returns the number of bytes per row for a plane at the specified index in the pixel buffer.
- [func CVPixelBufferGetHeight(CVPixelBuffer) -> Int](cvpixelbuffergetheight(_:).md)
  Returns the height of the pixel buffer.
- [func CVPixelBufferGetHeightOfPlane(CVPixelBuffer, Int) -> Int](cvpixelbuffergetheightofplane(_:_:).md)
  Returns the height of the plane at planeIndex in the pixel buffer.
- [func CVPixelBufferGetWidth(CVPixelBuffer) -> Int](cvpixelbuffergetwidth(_:).md)
  Returns the width of the pixel buffer.
- [func CVPixelBufferGetWidthOfPlane(CVPixelBuffer, Int) -> Int](cvpixelbuffergetwidthofplane(_:_:).md)
  Returns the width of the plane at a given index in the pixel buffer.
- [func CVPixelBufferIsPlanar(CVPixelBuffer) -> Bool](cvpixelbufferisplanar(_:).md)
  Determines whether the pixel buffer is planar.
- [func CVPixelBufferGetPlaneCount(CVPixelBuffer) -> Int](cvpixelbuffergetplanecount(_:).md)
  Returns number of planes of the pixel buffer.
- [func CVPixelBufferGetDataSize(CVPixelBuffer) -> Int](cvpixelbuffergetdatasize(_:).md)
  Returns the data size for contiguous planes of the pixel buffer.
- [func CVPixelBufferGetPixelFormatType(CVPixelBuffer) -> OSType](cvpixelbuffergetpixelformattype(_:).md)
  Returns the pixel format type of the pixel buffer.
- [func CVPixelBufferGetExtendedPixels(CVPixelBuffer, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?)](cvpixelbuffergetextendedpixels(_:_:_:_:_:).md)
  Returns the amount of extended pixel padding in the pixel buffer.
- [func CVPixelBufferGetIOSurface(CVPixelBuffer?) -> Unmanaged<IOSurfaceRef>?](cvpixelbuffergetiosurface(_:).md)
  Returns the IOSurface backing the pixel buffer, or `NULL` if it is not backed by an IOSurface.
- [func CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator?, CFArray?, UnsafeMutablePointer<CFDictionary?>) -> CVReturn](cvpixelbuffercreateresolvedattributesdictionary(_:_:_:).md)
  Resolves an array of `CFDictionary` objects describing various pixel buffer attributes into a single dictionary.
- [func CVPixelBufferGetTypeID() -> CFTypeID](cvpixelbuffergettypeid().md)
  Returns the Core Foundation type identifier of the pixel buffer type.
### Modifying Pixel Buffers
- [func CVPixelBufferFillExtendedPixels(CVPixelBuffer) -> CVReturn](cvpixelbufferfillextendedpixels(_:).md)
  Fills the extended pixels of the pixel buffer.
- [func CVPixelBufferLockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](cvpixelbufferlockbaseaddress(_:_:).md)
  Locks the base address of the pixel buffer.
- [func CVPixelBufferUnlockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](cvpixelbufferunlockbaseaddress(_:_:).md)
  Unlocks the base address of the pixel buffer.
### Data Types
- [typealias CVPixelBuffer](cvpixelbuffer.md)
  A reference to a Core Video pixel buffer object.
- [struct CVPixelBufferLockFlags](cvpixelbufferlockflags.md)
  The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md).
- [struct CVPlanarComponentInfo](cvplanarcomponentinfo.md)
  A structure for describing planar components.
- [struct CVPlanarPixelBufferInfo](cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.
### Callbacks
- [typealias CVPixelBufferReleaseBytesCallback](cvpixelbufferreleasebytescallback.md)
  A type that defines a release callback function.
- [typealias CVPixelBufferReleasePlanarBytesCallback](cvpixelbufferreleaseplanarbytescallback.md)
  Defines a pointer to a pixel buffer release callback function, which is called when a pixel buffer created by [`CVPixelBufferCreateWithPlanarBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) is released.
### Constants
- [Pixel Buffer Attribute Keys](pixel-buffer-attribute-keys.md)
  The attributes associated with a pixel buffer.

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [CVBuffer](cvbuffer-nfm.md)
  An abstract base class that defines how to interact with data buffers.
- [CVImageBuffer](cvimagebuffer-q40.md)
  An interface for managing different types of image data.
- [CVPixelBufferPool](cvpixelbufferpool-77o.md)
  A utility object for managing a recyclable set of pixel buffer objects.
- [CVPixelFormatDescription](cvpixelformatdescription.md)
  An API that provides functions and types for defining custom pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffer-q2e)*