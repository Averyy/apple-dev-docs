# CGPDFScannerPopStream(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Retrieves a PDF stream object from the scanner stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFScannerPopStream(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the stream object is retrieved successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `scanner`: A valid scanner object.
- `value`: On output, points to the PDF stream object popped from the scanner stack.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerpopstream(_:_:))*