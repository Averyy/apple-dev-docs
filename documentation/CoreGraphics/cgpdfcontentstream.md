# CGPDFContentStream

**Framework**: Core Graphics

A representation of one or more content data streams in a PDF page.

#### Overview

A [`CGPDFContentStreamRef`](cgpdfcontentstreamref.md) object represents one or more PDF content streams for a page and their associated resource dictionaries. A PDF content stream is a sequential set of instructions that specifies how to paint items on a PDF page. A resource dictionary contains information needed by the content stream in order to decode the sequential instructions of the content stream.

[`CGPDFContentStreamRef`](cgpdfcontentstreamref.md) functions can retrieve both the content streams and the resource dictionaries associated with a PDF page.

This type is not derived from [`CFTypeRef`](https://developer.apple.com/documentation/CoreFoundation/CFTypeRef) and therefore there are no functions for retaining and releasing it. [`CGPDFContentStreamRef`](cgpdfcontentstreamref.md) objects exist only as constituent parts of a [`CGPDFDocument`](cgpdfdocument.md) object, and they are managed by their container.

## Topics

### Creating a PDF Content Stream Object
- [func CGPDFContentStreamCreateWithPage(CGPDFPage) -> CGPDFContentStreamRef](cgpdfcontentstreamcreatewithpage(_:).md)
  Creates a content stream object from a PDF page object.
- [func CGPDFContentStreamCreateWithStream(CGPDFStreamRef, CGPDFDictionaryRef, CGPDFContentStreamRef) -> CGPDFContentStreamRef](cgpdfcontentstreamcreatewithstream(_:_:_:).md)
  Creates a PDF content stream object from an existing PDF content stream object.
### Getting Data from a PDF Content Stream Object
- [func CGPDFContentStreamGetStreams(CGPDFContentStreamRef) -> CFArray?](cgpdfcontentstreamgetstreams(_:).md)
  Gets the array of PDF content streams contained in a PDF content stream object.
- [func CGPDFContentStreamGetResource(CGPDFContentStreamRef, UnsafePointer<CChar>, UnsafePointer<CChar>) -> CGPDFObjectRef?](cgpdfcontentstreamgetresource(_:_:_:).md)
  Gets the specified resource from a PDF content stream object.
### Retaining and Releasing a PDF Content Stream Object
- [func CGPDFContentStreamRetain(CGPDFContentStreamRef) -> CGPDFContentStreamRef](cgpdfcontentstreamretain(_:).md)
  Increments the retain count of a PDF content stream object.
- [func CGPDFContentStreamRelease(CGPDFContentStreamRef)](cgpdfcontentstreamrelease(_:).md)
  Decrements the retain count of a PDF content stream object.
### Data Types
- [typealias CGPDFContentStreamRef](cgpdfcontentstreamref.md)
  An opaque type that provides access to the data that describes the appearance of a PDF page.

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstream)*