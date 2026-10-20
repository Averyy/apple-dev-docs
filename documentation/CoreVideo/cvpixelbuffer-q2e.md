# CVPixelBuffer

**Framework**: Core Video  
**Role**: API Collection

An image buffer that holds pixels in main memory.

#### Overview

A Core Video pixel buffer is an image buffer that holds pixels in main memory. Applications generating frames, compressing or decompressing video, or using Core Image can all make use of Core Video pixel buffers.

## Topics

### Creating pixel buffers
- [func CVPixelBufferCreate(CFAllocator?, Int, Int, OSType, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](./cvpixelbuffercreate%28_,_,_,_,_,_%29.md)
  Creates a single pixel buffer for a given size and pixel format.
- [func CVPixelBufferCreateWithBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer, Int, CVPixelBufferReleaseBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](./cvpixelbuffercreatewithbytes%28_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a pixel buffer for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithPlanarBytes(CFAllocator?, Int, Int, OSType, UnsafeMutableRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](./cvpixelbuffercreatewithplanarbytes%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a single pixel buffer in planar format for a given size and pixel format containing data specified by a memory location.
- [func CVPixelBufferCreateWithIOSurface(CFAllocator?, IOSurfaceRef, CFDictionary?, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn](./cvpixelbuffercreatewithiosurface%28_,_,_,_%29.md)
  Creates a single pixel buffer for the IO surface that you specify.
### Inspecting Pixel Buffers
- [func CVPixelBufferGetBaseAddress(CVPixelBuffer) -> UnsafeMutableRawPointer?](./cvpixelbuffergetbaseaddress%28_%29.md)
  Returns the base address of the pixel buffer.
- [func CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer, Int) -> UnsafeMutableRawPointer?](./cvpixelbuffergetbaseaddressofplane%28_,_%29.md)
  Returns the base address of the plane at the specified plane index.
- [func CVPixelBufferGetBytesPerRow(CVPixelBuffer) -> Int](./cvpixelbuffergetbytesperrow%28_%29.md)
  Returns the number of bytes per row of the pixel buffer.
- [func CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer, Int) -> Int](./cvpixelbuffergetbytesperrowofplane%28_,_%29.md)
  Returns the number of bytes per row for a plane at the specified index in the pixel buffer.
- [func CVPixelBufferGetHeight(CVPixelBuffer) -> Int](./cvpixelbuffergetheight%28_%29.md)
  Returns the height of the pixel buffer.
- [func CVPixelBufferGetHeightOfPlane(CVPixelBuffer, Int) -> Int](./cvpixelbuffergetheightofplane%28_,_%29.md)
  Returns the height of the plane at planeIndex in the pixel buffer.
- [func CVPixelBufferGetWidth(CVPixelBuffer) -> Int](./cvpixelbuffergetwidth%28_%29.md)
  Returns the width of the pixel buffer.
- [func CVPixelBufferGetWidthOfPlane(CVPixelBuffer, Int) -> Int](./cvpixelbuffergetwidthofplane%28_,_%29.md)
  Returns the width of the plane at a given index in the pixel buffer.
- [func CVPixelBufferIsPlanar(CVPixelBuffer) -> Bool](./cvpixelbufferisplanar%28_%29.md)
  Determines whether the pixel buffer is planar.
- [func CVPixelBufferGetPlaneCount(CVPixelBuffer) -> Int](./cvpixelbuffergetplanecount%28_%29.md)
  Returns number of planes of the pixel buffer.
- [func CVPixelBufferGetDataSize(CVPixelBuffer) -> Int](./cvpixelbuffergetdatasize%28_%29.md)
  Returns the data size for contiguous planes of the pixel buffer.
- [func CVPixelBufferGetPixelFormatType(CVPixelBuffer) -> OSType](./cvpixelbuffergetpixelformattype%28_%29.md)
  Returns the pixel format type of the pixel buffer.
- [func CVPixelBufferGetExtendedPixels(CVPixelBuffer, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?)](./cvpixelbuffergetextendedpixels%28_,_,_,_,_%29.md)
  Returns the amount of extended pixel padding in the pixel buffer.
- [func CVPixelBufferGetIOSurface(CVPixelBuffer?) -> Unmanaged<IOSurfaceRef>?](./cvpixelbuffergetiosurface%28_%29.md)
  Returns the IOSurface backing the pixel buffer, or `NULL` if it is not backed by an IOSurface.
- [func CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator?, CFArray?, UnsafeMutablePointer<CFDictionary?>) -> CVReturn](./cvpixelbuffercreateresolvedattributesdictionary%28_,_,_%29.md)
  Resolves an array of `CFDictionary` objects describing various pixel buffer attributes into a single dictionary.
- [func CVPixelBufferIsCompatibleWithAttributes(CVPixelBuffer, CFDictionary?) -> Bool](./cvpixelbufferiscompatiblewithattributes%28_,_%29.md)
- [func CVPixelBufferGetTypeID() -> CFTypeID](./cvpixelbuffergettypeid%28%29.md)
  Returns the Core Foundation type identifier of the pixel buffer type.
### Modifying Pixel Buffers
- [func CVPixelBufferFillExtendedPixels(CVPixelBuffer) -> CVReturn](./cvpixelbufferfillextendedpixels%28_%29.md)
  Fills the extended pixels of the pixel buffer.
- [func CVPixelBufferLockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](./cvpixelbufferlockbaseaddress%28_,_%29.md)
  Locks the base address of the pixel buffer.
- [func CVPixelBufferUnlockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](./cvpixelbufferunlockbaseaddress%28_,_%29.md)
  Unlocks the base address of the pixel buffer.
### Protocols
- [protocol CVPixelBufferRepresentable](./cvpixelbufferrepresentable.md)
  CVPixelBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVPixelBuffer type.
- [enum CVPixelBufferAttachmentKeyDefinitions](./cvpixelbufferattachmentkeydefinitions.md)
  A namespace for pixel buffer attachment keys.
### Swift overlay types
- [class CVReadOnlyPixelBuffer](./cvreadonlypixelbuffer.md)
  CVReadOnlyPixelBuffer provides an immutable view of the pixel data held by the pixel buffer.
- [struct CVMutablePixelBuffer](./cvmutablepixelbuffer.md)
  CVMutablePixelBuffer provides read-write access to the pixel data and attachments.
- [struct CVPixelBufferAttributes](./cvpixelbufferattributes.md)
  A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.
- [struct CVPixelBufferCreationAttributes](./cvpixelbuffercreationattributes.md)
  Attributes needed for creating a pixel buffer.
- [struct CVPixelBufferPadding](./cvpixelbufferpadding.md)
  Padding pixels around the CVPixelBuffer
- [struct CVPixelBufferPlaneProperties](./cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer
- [struct CVProResRawMetadata](./cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.
### Data Types
- [typealias CVPixelBuffer](./cvpixelbuffer.md)
  A reference to a Core Video pixel buffer object.
- [struct CVPixelBufferLockFlags](./cvpixelbufferlockflags.md)
  The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](./cvpixelbufferlockbaseaddress%28_,_%29.md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](./cvpixelbufferunlockbaseaddress%28_,_%29.md).
- [struct CVPlanarComponentInfo](./cvplanarcomponentinfo.md)
  A structure for describing planar components.
- [struct CVPlanarPixelBufferInfo](./cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](./cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](./cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.
### Callbacks
- [typealias CVPixelBufferReleaseBytesCallback](./cvpixelbufferreleasebytescallback.md)
  A type that defines a release callback function.
- [typealias CVPixelBufferReleasePlanarBytesCallback](./cvpixelbufferreleaseplanarbytescallback.md)
  Defines a pointer to a pixel buffer release callback function, which is called when a pixel buffer created by [`CVPixelBufferCreateWithPlanarBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](./cvpixelbuffercreatewithplanarbytes%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md) is released.
### Constants
- [Pixel Buffer Attribute Keys](./pixel-buffer-attribute-keys.md)
  The attributes associated with a pixel buffer.

## See Also

### Related Documentation
- [Core Video Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
### Data Processing
- [CVBuffer](./cvbuffer-nfm.md)
  An abstract base class that defines how to interact with data buffers.
- [CVImageBuffer](./cvimagebuffer-q40.md)
  An interface for managing different types of image data.
- [CVPixelBufferPool](./cvpixelbufferpool-77o.md)
  A utility object for managing a recyclable set of pixel buffer objects.
- [CVPixelFormatDescription](./cvpixelformatdescription-42p.md)
  An API that provides functions and types for defining custom pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffer-q2e)*