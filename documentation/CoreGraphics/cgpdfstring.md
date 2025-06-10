# CGPDFString

**Framework**: Core Graphics

A text string in a PDF document.

#### Overview

A PDF string object is a series of bytes—unsigned integer values in the range 0 to 255.

The string elements are not integer objects, but are stored in a more compact format. For more information on the representation of strings in PDF, see the latest version of , Adobe Systems Incorporated.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFString objects exist as constituent parts of a CGPDFDocument object, and are managed by their container.

## Topics

### Converting PDF Strings
- [func CGPDFStringCopyTextString(CGPDFStringRef) -> CFString?](cgpdfstringcopytextstring(_:).md)
  Returns a CFString object that represents a PDF string as a text string.
- [func CGPDFStringCopyDate(CGPDFStringRef) -> CFDate?](cgpdfstringcopydate(_:).md)
  Converts a string to a date.
### Getting PDF String Data
- [func CGPDFStringGetBytePtr(CGPDFStringRef) -> UnsafePointer<UInt8>?](cgpdfstringgetbyteptr(_:).md)
  Returns a pointer to the bytes of a PDF string.
- [func CGPDFStringGetLength(CGPDFStringRef) -> Int](cgpdfstringgetlength(_:).md)
  Returns the number of bytes in a PDF string.
### Data Types
- [struct CGPDFStringRef](cgpdfstringref.md)
  A data type that represents a string in a PDF document.

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstring)*