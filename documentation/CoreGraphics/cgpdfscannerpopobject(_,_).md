# CGPDFScannerPopObject(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Retrieves an object from the scanner stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFScannerPopObject(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool
```

```c
extern bool CGPDFScannerPopObject(CGPDFScannerRef scanner, CGPDFObjectRef*value);
```

#### Return Value

[`true`](../Swift/true.md) if the object is retrieved successfully; otherwise, [`false`](../Swift/false.md).

## Parameters

- `scanner`: A valid scanner object.
- `value`: On output, points to the object popped from the scanner stack.

## See Also

### Getting PDF Objects from the Scanner Stack
- [func CGPDFScannerPopBoolean(CGPDFScannerRef, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfscannerpopboolean%28_,_%29.md)
  Retrieves a Boolean object from the scanner stack.
- [func CGPDFScannerPopInteger(CGPDFScannerRef, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](./cgpdfscannerpopinteger%28_,_%29.md)
  Retrieves an integer object from the scanner stack.
- [func CGPDFScannerPopNumber(CGPDFScannerRef, UnsafeMutablePointer<CGPDFReal>?) -> Bool](./cgpdfscannerpopnumber%28_,_%29.md)
  Retrieves a real value object from the scanner stack.
- [func CGPDFScannerPopName(CGPDFScannerRef, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](./cgpdfscannerpopname%28_,_%29.md)
  Retrieves a character string from the scanner stack.
- [func CGPDFScannerPopString(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfscannerpopstring%28_,_%29.md)
  Retrieves a string object from the scanner stack.
- [func CGPDFScannerPopArray(CGPDFScannerRef, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfscannerpoparray%28_,_%29.md)
  Retrieves an array object from the scanner stack.
- [func CGPDFScannerPopDictionary(CGPDFScannerRef, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](./cgpdfscannerpopdictionary%28_,_%29.md)
  Retrieves a PDF dictionary object from the scanner stack.
- [func CGPDFScannerPopStream(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](./cgpdfscannerpopstream%28_,_%29.md)
  Retrieves a PDF stream object from the scanner stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerpopobject(_:_:))*