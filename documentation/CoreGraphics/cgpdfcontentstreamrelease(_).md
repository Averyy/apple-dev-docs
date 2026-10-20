# CGPDFContentStreamRelease(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a PDF content stream object.

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
func CGPDFContentStreamRelease(_ cs: CGPDFContentStreamRef)
```

```c
extern void CGPDFContentStreamRelease(CGPDFContentStreamRef cs);
```

## Parameters

- `cs`: A PDF content stream.

## See Also

### Retaining and Releasing a PDF Content Stream Object
- [func CGPDFContentStreamRetain(CGPDFContentStreamRef) -> CGPDFContentStreamRef](./cgpdfcontentstreamretain%28_%29.md)
  Increments the retain count of a PDF content stream object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamrelease(_:))*