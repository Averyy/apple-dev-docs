# CGPDFObject

**Framework**: Core Graphics

An object representing content within a PDF document.

#### Overview

PDF supports several basic types of object: Boolean values, integer and real numbers, strings, names, arrays, dictionaries, and streams. Most of these are represented in Core Graphics by corresponding specific types. A CGPDFObject can represent any of these types. You use CGPDFObject functions to determine the type of the object, and retrieve the object value if it is of an expected type.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFObject objects exist as constituent parts of a CGPDFDocument object, and are managed by their container.

## Topics

### Getting Object Types and Values
- [func CGPDFObjectGetType(CGPDFObjectRef) -> CGPDFObjectType](cgpdfobjectgettype(_:).md)
  Returns the PDF type identifier of an object.
- [func CGPDFObjectGetValue(CGPDFObjectRef, CGPDFObjectType, UnsafeMutableRawPointer?) -> Bool](cgpdfobjectgetvalue(_:_:_:).md)
  Returns whether an object is of a given type and if it is, retrieves its value.
### Data Types
- [struct CGPDFObjectRef](cgpdfobjectref.md)
  A type that contains information about a PDF object.
- [typealias CGPDFBoolean](cgpdfboolean.md)
  A PDF Boolean value.
- [typealias CGPDFInteger](cgpdfinteger.md)
  A PDF integer value.
- [typealias CGPDFReal](cgpdfreal.md)
  A PDF real value.
### Constants
- [enum CGPDFObjectType](cgpdfobjecttype.md)
  Types of PDF object.

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfobject)*