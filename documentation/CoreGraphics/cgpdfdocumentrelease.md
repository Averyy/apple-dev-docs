# CGPDFDocumentRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a PDF document.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGPDFDocumentRelease(CGPDFDocumentRef document);
```

## Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `document` parameter is `NULL`.

## Parameters

- `document`: The PDF document to release.

## See Also

### Retaining and Releasing PDF Documents
- [CGPDFDocumentRetain](./cgpdfdocumentretain.md)
  Increments the retain count of a Core Graphics PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentrelease)*