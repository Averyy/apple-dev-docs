# quadrilateralPoints

**Framework**: PDFKit  
**Kind**: property

An array of values that represents the points bounding the marked-up text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var quadrilateralPoints: [NSValue]? { get set }
```

#### Discussion

The array contains `N * 4` [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects that use [`pointValue`](https://developer.apple.com/documentation/foundation/nsvalue/1391255-pointvalue) or [`cgPointValue`](https://developer.apple.com/documentation/foundation/nsvalue/1624534-cgpointvalue) to define `N` quadrilaterals in page-space coordinates, where `N` is the number of quad points. The order of the points is a Z pattern as follows:

- Upper-left point
- Upper-right point
- Lower-left point
- Lower-right point

The coordinates of each point are relative to the bound’s origin of the annotation.

## See Also

- [var markupType: PDFMarkupType](pdfannotation/markuptype.md)
  The markup type that the annotation displays, either highlight, strikethrough, underline, or redact.
- [enum PDFMarkupType](pdfmarkuptype.md)
  The styles available for markup annotations in PDFKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/quadrilateralpoints)*