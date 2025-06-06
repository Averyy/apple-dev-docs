# CGPDFStreamCopyData(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns the data associated with a PDF stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFStreamCopyData(_ stream: CGPDFStreamRef, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> CFData?
```

#### Return Value

A CFData object that contains a copy of the stream data. You are responsible for releasing this object.

## Parameters

- `stream`: A PDF stream.
- `format`: On return, contains a constant that specifies the format of the data returned— ,  , or  .

## See Also

- [func CGPDFStreamGetDictionary(CGPDFStreamRef) -> CGPDFDictionaryRef?](cgpdfstreamgetdictionary(_:).md)
  Returns the dictionary associated with a PDF stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstreamcopydata(_:_:))*