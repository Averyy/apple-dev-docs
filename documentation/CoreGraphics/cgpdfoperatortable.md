# CGPDFOperatorTable

**Framework**: Core Graphics

A set of callback functions for operators used when scanning content in a PDF document.

#### Overview

You pass an operator table and a PDF content stream to a CGPDFScanner object. When the scanner parses a PDF operator, Core Graphics invokes your callback for that operator. See also [`CGPDFScanner`](cgpdfscanner.md) and [`CGPDFContentStream`](cgpdfcontentstream.md).

> **Note**:  This object is not derived from CFType and therefore you can’t use the Core Foundation base functions on it, such as [`CFRetain`](https://developer.apple.com/documentation/CoreFoundation/CFRetain) and [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease). In Objective-C, handle memory management with [`CGPDFOperatorTableRetain(_:)`](cgpdfoperatortableretain(_:).md) and [`CGPDFOperatorTableRelease(_:)`](cgpdfoperatortablerelease(_:).md).

For more about PDF operators, see the latest version of , Adobe Systems Incorporated.

## Topics

### Creating a PDF Operator Table
- [func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef?](cgpdfoperatortablecreate().md)
  Creates an empty PDF operator table.
### Setting Callback Functions
- [func CGPDFOperatorTableSetCallback(CGPDFOperatorTableRef, UnsafePointer<CChar>, CGPDFOperatorCallback)](cgpdfoperatortablesetcallback(_:_:_:).md)
  Sets a callback function for a PDF operator.
### Retaining and Releasing a PDF Operator Table
- [func CGPDFOperatorTableRetain(CGPDFOperatorTableRef) -> CGPDFOperatorTableRef](cgpdfoperatortableretain(_:).md)
  Increments the retain count of a CGPDFOperatorTable object.
- [func CGPDFOperatorTableRelease(CGPDFOperatorTableRef)](cgpdfoperatortablerelease(_:).md)
  Decrements the retain count of a CGPDFOperatorTable object.
### Callbacks
- [typealias CGPDFOperatorCallback](cgpdfoperatorcallback.md)
  Performs custom processing for PDF operators.
### Data Types
- [typealias CGPDFOperatorTableRef](cgpdfoperatortableref.md)
  A type that stores callback functions for PDF operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortable)*