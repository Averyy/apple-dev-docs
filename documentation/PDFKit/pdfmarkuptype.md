# PDFMarkupType

**Framework**: PDFKit  
**Kind**: enum

The styles available for markup annotations in PDFKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum PDFMarkupType
```

## Topics

### Constants
- [PDFMarkupType.highlight](pdfmarkuptype/highlight.md)
  Highlight style for the markup.
- [PDFMarkupType.strikeOut](pdfmarkuptype/strikeout.md)
  Strikethrough style for the markup.
- [PDFMarkupType.underline](pdfmarkuptype/underline.md)
  Underline style for the markup.
- [PDFMarkupType.redact](pdfmarkuptype/redact.md)
  The redaction style for markup.
### Initializers
- [init?(rawValue: Int)](pdfmarkuptype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var markupType: PDFMarkupType](pdfannotation/markuptype.md)
  The markup type that the annotation displays, either highlight, strikethrough, underline, or redact.
- [var quadrilateralPoints: [NSValue]?](pdfannotation/quadrilateralpoints.md)
  An array of values that represents the points bounding the marked-up text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfmarkuptype)*