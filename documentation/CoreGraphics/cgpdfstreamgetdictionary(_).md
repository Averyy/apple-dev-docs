# CGPDFStreamGetDictionary(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the dictionary associated with a PDF stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef?
```

```c
extern CGPDFDictionaryRefCGPDFStreamGetDictionary(CGPDFStreamRef stream);
```

#### Return Value

The PDF dictionary for the specified stream.

## Parameters

- `stream`: A PDF stream.

## See Also

### Getting Data from a PDF Stream
- [func CGPDFStreamCopyData(CGPDFStreamRef, UnsafeMutablePointer<CGPDFDataFormat>) -> CFData?](./cgpdfstreamcopydata%28_,_%29.md)
  Returns the data associated with a PDF stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstreamgetdictionary(_:))*