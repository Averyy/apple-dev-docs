# CGPDFOperatorTable

**Framework**: Core Graphics  
**Role**: API Collection

A set of callback functions for operators used when scanning content in a PDF document.

#### Overview

You pass an operator table and a PDF content stream to a CGPDFScanner object. When the scanner parses a PDF operator, Core Graphics invokes your callback for that operator. See also [CGPDFScanner](./cgpdfscanner.md) and [CGPDFContentStream](./cgpdfcontentstream.md).

> **Note**:  This object is not derived from CFType and therefore you can’t use the Core Foundation base functions on it, such as [`CFRetain`](../CoreFoundation/cfretain.md) and [`CFRelease`](../CoreFoundation/cfrelease.md). In Objective-C, handle memory management with [`CGPDFOperatorTableRetain(_:)`](./cgpdfoperatortableretain%28_%29.md) and [`CGPDFOperatorTableRelease(_:)`](./cgpdfoperatortablerelease%28_%29.md).

For more about PDF operators, see the latest version of *PDF Reference*, Adobe Systems Incorporated.

## Topics

### Creating a PDF Operator Table
- [func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef?](./cgpdfoperatortablecreate%28%29.md)
  Creates an empty PDF operator table.
### Setting Callback Functions
- [func CGPDFOperatorTableSetCallback(CGPDFOperatorTableRef, UnsafePointer<CChar>, CGPDFOperatorCallback)](./cgpdfoperatortablesetcallback%28_,_,_%29.md)
  Sets a callback function for a PDF operator.
### Retaining and Releasing a PDF Operator Table
- [func CGPDFOperatorTableRetain(CGPDFOperatorTableRef) -> CGPDFOperatorTableRef](./cgpdfoperatortableretain%28_%29.md)
  Increments the retain count of a CGPDFOperatorTable object.
- [func CGPDFOperatorTableRelease(CGPDFOperatorTableRef)](./cgpdfoperatortablerelease%28_%29.md)
  Decrements the retain count of a CGPDFOperatorTable object.
### Callbacks
- [typealias CGPDFOperatorCallback](./cgpdfoperatorcallback.md)
  Performs custom processing for PDF operators.
### Data Types
- [typealias CGPDFOperatorTableRef](./cgpdfoperatortableref.md)
  A type that stores callback functions for PDF operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortable)*