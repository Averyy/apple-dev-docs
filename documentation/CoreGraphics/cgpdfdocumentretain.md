# CGPDFDocumentRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a Core Graphics PDF document.

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
extern CGPDFDocumentRefCGPDFDocumentRetain(CGPDFDocumentRef document);
```

#### Return Value

The same document you passed in as the `document` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `document` parameter is `NULL`.

## Parameters

- `document`: The PDF document to retain.

## See Also

### Retaining and Releasing PDF Documents
- [CGPDFDocumentRelease](./cgpdfdocumentrelease.md)
  Decrements the retain count of a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentretain)*