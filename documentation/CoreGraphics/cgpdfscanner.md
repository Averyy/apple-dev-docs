# CGPDFScanner

**Framework**: Core Graphics

A parser object for handling content and operators in a PDF content stream.

#### Overview

You can set up the PDF scanner object to invoke callbacks when it encounters specific PDF operators in the stream.

This object is not derived from `CFType`. In Objective-C, use [`CGPDFScannerRetain(_:)`](cgpdfscannerretain(_:).md) and [`CGPDFScannerRelease(_:)`](cgpdfscannerrelease(_:).md) to manage the retain count of [`CGPDFScannerRef`](cgpdfscannerref.md) instances; do not use [`CFRetain`](https://developer.apple.com/documentation/corefoundation/1521269-cfretain) and [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

## Topics

### Creating a PDF Scanner Object
- [func CGPDFScannerCreate(CGPDFContentStreamRef, CGPDFOperatorTableRef?, UnsafeMutableRawPointer?) -> CGPDFScannerRef](cgpdfscannercreate(_:_:_:).md)
  Creates a PDF scanner.
### Retaining and Releasing PDF Scanner Objects
- [func CGPDFScannerRetain(CGPDFScannerRef) -> CGPDFScannerRef](cgpdfscannerretain(_:).md)
  Increments the retain count of a scanner object.
- [func CGPDFScannerRelease(CGPDFScannerRef)](cgpdfscannerrelease(_:).md)
  Decrements the retain count of a scanner object.
### Parsing Content
- [func CGPDFScannerScan(CGPDFScannerRef) -> Bool](cgpdfscannerscan(_:).md)
  Parses the content stream of a PDF scanner object.
- [func CGPDFScannerGetContentStream(CGPDFScannerRef) -> CGPDFContentStreamRef](cgpdfscannergetcontentstream(_:).md)
  Returns the content stream associated with a PDF scanner object.
### Getting PDF Objects from the Scanner Stack
- [func CGPDFScannerPopObject(CGPDFScannerRef, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](cgpdfscannerpopobject(_:_:).md)
  Retrieves an object from the scanner stack.
- [func CGPDFScannerPopBoolean(CGPDFScannerRef, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](cgpdfscannerpopboolean(_:_:).md)
  Retrieves a Boolean object from the scanner stack.
- [func CGPDFScannerPopInteger(CGPDFScannerRef, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](cgpdfscannerpopinteger(_:_:).md)
  Retrieves an integer object from the scanner stack.
- [func CGPDFScannerPopNumber(CGPDFScannerRef, UnsafeMutablePointer<CGPDFReal>?) -> Bool](cgpdfscannerpopnumber(_:_:).md)
  Retrieves a real value object from the scanner stack.
- [func CGPDFScannerPopName(CGPDFScannerRef, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](cgpdfscannerpopname(_:_:).md)
  Retrieves a character string from the scanner stack.
- [func CGPDFScannerPopString(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](cgpdfscannerpopstring(_:_:).md)
  Retrieves a string object from the scanner stack.
- [func CGPDFScannerPopArray(CGPDFScannerRef, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](cgpdfscannerpoparray(_:_:).md)
  Retrieves an array object from the scanner stack.
- [func CGPDFScannerPopDictionary(CGPDFScannerRef, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](cgpdfscannerpopdictionary(_:_:).md)
  Retrieves a PDF dictionary object from the scanner stack.
- [func CGPDFScannerPopStream(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](cgpdfscannerpopstream(_:_:).md)
  Retrieves a PDF stream object from the scanner stack.
### Data Types
- [typealias CGPDFScannerRef](cgpdfscannerref.md)
  A type used to parse a PDF content stream.

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscanner)*