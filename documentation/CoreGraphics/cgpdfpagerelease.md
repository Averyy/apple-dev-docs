# CGPDFPageRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a PDF page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGPDFPageRelease(CGPDFPageRef page);
```

#### Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `page` parameter is `NULL`.

## Parameters

- `page`: A PDF page.

## See Also

### Retaining and Releasing a PDF Page
- [CGPDFPageRetain](./cgpdfpageretain.md)
  Increments the retain count of a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpagerelease)*