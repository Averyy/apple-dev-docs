# CGPDFContentStreamGetStreams(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Gets the array of PDF content streams contained in a PDF content stream object.

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
func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStreamRef) -> CFArray?
```

```c
extern CFArrayRefCGPDFContentStreamGetStreams(CGPDFContentStreamRef cs);
```

## Return Value

The array of PDF content streams that make up the content stream object represented by the `cs` parameter.

## Parameters

- `cs`: A PDF content stream object.

## See Also

### Getting Data from a PDF Content Stream Object
- [func CGPDFContentStreamGetResource(CGPDFContentStreamRef, UnsafePointer<CChar>, UnsafePointer<CChar>) -> CGPDFObjectRef?](./cgpdfcontentstreamgetresource%28_,_,_%29.md)
  Gets the specified resource from a PDF content stream object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamgetstreams(_:))*