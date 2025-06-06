# CGPDFContentStreamRetain(_:)

**Framework**: Core Graphics  
**Kind**: func

Increments the retain count of a PDF content stream object.

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
func CGPDFContentStreamRetain(_ cs: CGPDFContentStreamRef) -> CGPDFContentStreamRef
```

#### Return Value

The same PDF content stream you passed in as the `cs` parameter.

## Parameters

- `cs`: A PDF content stream object.

## See Also

- [func CGPDFContentStreamRelease(CGPDFContentStreamRef)](cgpdfcontentstreamrelease(_:).md)
  Decrements the retain count of a PDF content stream object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamretain(_:))*