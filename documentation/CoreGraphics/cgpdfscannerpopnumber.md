# CGPDFScannerPopNumber(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Retrieves a real value object from the scanner stack.

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
func CGPDFScannerPopNumber(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFReal>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the real value is retrieved successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The number retrieved from the scanner can be a real value or an integer value. However, the result is always converted to a value of type [`CGPDFReal`](cgpdfreal.md).

## Parameters

- `scanner`: A valid scanner object.
- `value`: On output, points to the real value object popped from the scanner stack.

## See Also

- [func CGPDFScannerPopObject(CGPDFScannerRef, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](cgpdfscannerpopobject(_:_:).md)
  Retrieves an object from the scanner stack.
- [func CGPDFScannerPopBoolean(CGPDFScannerRef, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](cgpdfscannerpopboolean(_:_:).md)
  Retrieves a Boolean object from the scanner stack.
- [func CGPDFScannerPopInteger(CGPDFScannerRef, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](cgpdfscannerpopinteger(_:_:).md)
  Retrieves an integer object from the scanner stack.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerpopnumber(_:_:))*