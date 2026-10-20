# CGPDFContentStreamRetain(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a PDF content stream object.

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
func CGPDFContentStreamRetain(_ cs: CGPDFContentStreamRef) -> CGPDFContentStreamRef
```

```c
extern CGPDFContentStreamRefCGPDFContentStreamRetain(CGPDFContentStreamRef cs);
```

#### Return Value

The same PDF content stream you passed in as the `cs` parameter.

## Parameters

- `cs`: A PDF content stream object.

## See Also

### Retaining and Releasing a PDF Content Stream Object
- [func CGPDFContentStreamRelease(CGPDFContentStreamRef)](./cgpdfcontentstreamrelease%28_%29.md)
  Decrements the retain count of a PDF content stream object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamretain(_:))*