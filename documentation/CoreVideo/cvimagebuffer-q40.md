# CVImageBuffer

**Framework**: Core Video

An interface for managing different types of image data.

#### Overview

Core Video image buffers provides a convenient interface for managing different types of image data. Pixel buffers and Core Video OpenGL buffers derive from the Core Video image buffer.

## Topics

### Inspecting image buffers
- [func CVImageBufferGetCleanRect(CVImageBuffer) -> CGRect](cvimagebuffergetcleanrect(_:).md)
  Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.
- [func CVImageBufferGetColorSpace(CVImageBuffer) -> Unmanaged<CGColorSpace>?](cvimagebuffergetcolorspace(_:).md)
  Returns the color space of a Core Video image buffer.
- [func CVImageBufferGetDisplaySize(CVImageBuffer) -> CGSize](cvimagebuffergetdisplaysize(_:).md)
  Returns the nominal output display size, in square pixels, of a Core Video image buffer.
- [func CVImageBufferGetEncodedSize(CVImageBuffer) -> CGSize](cvimagebuffergetencodedsize(_:).md)
  Returns the full encoded dimensions of a Core Video image buffer.
- [func CVImageBufferIsFlipped(CVImageBuffer) -> Bool](cvimagebufferisflipped(_:).md)
  Returns a Boolean value indicating whether the image is vertically flipped.
### Creating color spaces
- [func CVImageBufferCreateColorSpaceFromAttachments(CFDictionary) -> Unmanaged<CGColorSpace>?](cvimagebuffercreatecolorspacefromattachments(_:).md)
  Attempts to create a Core Graphics color space from the image buffer’s attachments that you specify.
### Data types
- [typealias CVImageBuffer](cvimagebuffer.md)
  A reference to a Core Video image buffer.
### Converting between strings and integer code points
- [func CVColorPrimariesGetIntegerCodePointForString(CFString?) -> Int32](cvcolorprimariesgetintegercodepointforstring(_:).md)
  Returns the standard integer code point corresponding to the Core Video color primaries constant string that you specify.
- [func CVColorPrimariesGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](cvcolorprimariesgetstringforintegercodepoint(_:).md)
  Returns the Core Video color primaries string corresponding to the standard integer code point that you specify.
- [func CVTransferFunctionGetIntegerCodePointForString(CFString?) -> Int32](cvtransferfunctiongetintegercodepointforstring(_:).md)
  Returns the standard integer code point corresponding to the Core Video transfer function string that you specify.
- [func CVTransferFunctionGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](cvtransferfunctiongetstringforintegercodepoint(_:).md)
  Returns the Core Video transfer function string corresponding to the standard integer code point that you specify.
- [func CVYCbCrMatrixGetIntegerCodePointForString(CFString?) -> Int32](cvycbcrmatrixgetintegercodepointforstring(_:).md)
  Returns the standard integer code point corresponding to the Core Video YCbCr matrix string that you specify.
- [func CVYCbCrMatrixGetStringForIntegerCodePoint(Int32) -> Unmanaged<CFString>?](cvycbcrmatrixgetstringforintegercodepoint(_:).md)
  Returns the Core Video YCbCr matrix string corresponding to the standard integer code point that you specify.
### Constants
- [Image Buffer Attachment Keys](image-buffer-attachment-keys.md)
  Keys that describe the attachment types associated with image buffers.
- [Image Buffer Clean Aperture Keys](image-buffer-clean-aperture-keys.md)
  Keys that describe the clean aperture of an image buffer.
- [Image Buffer Pixel Aspect Ratio Keys](image-buffer-pixel-aspect-ratio-keys.md)
  Keys that describe the pixel aspect ratio of an image buffer.
- [Image Buffer Display Dimensions Keys](image-buffer-display-dimensions-keys.md)
  Keys that describe the display dimensions of an image buffer.
- [Image Buffer Field Detail Constants](image-buffer-field-detail-constants.md)
  Constants that indicate the field order of interlaced video in an image buffer.
- [Image Buffer YCbCr Matrix Constants](image-buffer-ycbcr-matrix-constants.md)
  Constants that indicate the type of conversion matrix Core Video uses when it converts image buffer data from the YCbCr color space to the RGB color space.
- [Image Buffer Color Primaries Constants](image-buffer-color-primaries-constants.md)
  Constants that indicate the color primaries gamut for the image buffer.
- [Image Buffer Transfer Function Constants](image-buffer-transfer-function-constants.md)
  Constants that indicate the transfer function for the image buffer.
- [Image Buffer Chroma Location Constants](image-buffer-chroma-location-constants.md)
  Constants that indicate locations for chroma samples in the image buffer.
- [Image Buffer Chroma Subsampling Constants](image-buffer-chroma-subsampling-constants.md)
  Constants that indicate the original format of subsampled data in the image buffer before conversion to 422/2vuy format.
- [Image Buffer Display Mask Rectangle Keys](image-buffer-display-mask-rectangle-keys.md)
  Keys that describe the display dimensions of an image buffer mask.

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [CVBuffer](cvbuffer-nfm.md)
  An abstract base class that defines how to interact with data buffers.
- [CVPixelBuffer](cvpixelbuffer-q2e.md)
  An image buffer that holds pixels in main memory.
- [CVPixelBufferPool](cvpixelbufferpool-77o.md)
  A utility object for managing a recyclable set of pixel buffer objects.
- [CVPixelFormatDescription](cvpixelformatdescription.md)
  An API that provides functions and types for defining custom pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffer-q40)*