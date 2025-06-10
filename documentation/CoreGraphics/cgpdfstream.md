# CGPDFStream

**Framework**: Core Graphics

A stream or sequence of data bytes in a PDF document.

#### Overview

A PDF stream  consists  of a dictionary that describes a sequence of bytes. Streams typically represent objects with potentially large amounts of data, such as images and page descriptions.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it.

## Topics

### Getting Data from a PDF Stream
- [func CGPDFStreamCopyData(CGPDFStreamRef, UnsafeMutablePointer<CGPDFDataFormat>) -> CFData?](cgpdfstreamcopydata(_:_:).md)
  Returns the data associated with a PDF stream.
- [func CGPDFStreamGetDictionary(CGPDFStreamRef) -> CGPDFDictionaryRef?](cgpdfstreamgetdictionary(_:).md)
  Returns the dictionary associated with a PDF stream.
### Data Types
- [struct CGPDFStreamRef](cgpdfstreamref.md)
  A type that represents a PDF stream.
### Constants
- [enum CGPDFDataFormat](cgpdfdataformat.md)
  The encoding format of PDF data.

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstream)*