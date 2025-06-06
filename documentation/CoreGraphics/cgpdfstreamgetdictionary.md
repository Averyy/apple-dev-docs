# CGPDFStreamGetDictionary(_:)

**Framework**: Core Graphics  
**Kind**: func

Returns the dictionary associated with a PDF stream.

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
func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef?
```

#### Return Value

The PDF dictionary for the specified stream.

## Parameters

- `stream`: A PDF stream.

## See Also

- [func CGPDFStreamCopyData(CGPDFStreamRef, UnsafeMutablePointer<CGPDFDataFormat>) -> CFData?](cgpdfstreamcopydata(_:_:).md)
  Returns the data associated with a PDF stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstreamgetdictionary(_:))*