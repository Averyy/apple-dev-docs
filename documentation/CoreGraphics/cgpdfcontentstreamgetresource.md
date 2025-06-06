# CGPDFContentStreamGetResource(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Gets the specified resource from a PDF content stream object.

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
func CGPDFContentStreamGetResource(_ cs: CGPDFContentStreamRef, _ category: UnsafePointer<CChar>, _ name: UnsafePointer<CChar>) -> CGPDFObjectRef?
```

#### Return Value

The resource dictionary.

#### Discussion

You can use this function to obtain resources used by the content stream, such as forms, patterns, color spaces, and fonts.

## Parameters

- `cs`: A PDF content stream object.
- `category`: A string that specifies the category of the resource you want to obtain.
- `name`: A string that specifies the name of the resource you want to obtain.

## See Also

- [func CGPDFContentStreamGetStreams(CGPDFContentStreamRef) -> CFArray?](cgpdfcontentstreamgetstreams(_:).md)
  Gets the array of PDF content streams contained in a PDF content stream object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamgetresource(_:_:_:))*