# CGPDFPageRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a PDF page.

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
extern CGPDFPageRefCGPDFPageRetain(CGPDFPageRef page);
```

## Return Value

The same page you passed in as the `page` parameter.

## Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `page` parameter is `NULL`.

## Parameters

- `page`: A PDF page.

## See Also

### Retaining and Releasing a PDF Page
- [CGPDFPageRelease](./cgpdfpagerelease.md)
  Decrements the retain count of a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpageretain)*