# PDFLineStyle

**Framework**: PDFKit  
**Kind**: enum

The following constants specify the available line ending styles.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum PDFLineStyle
```

## Topics

### Constants
- [PDFLineStyle.none](pdflinestyle/none.md)
  No line ending.
- [PDFLineStyle.square](pdflinestyle/square.md)
  A square line ending filled with the annotation’s interior color, if any.
- [PDFLineStyle.circle](pdflinestyle/circle.md)
  A circular line ending filled with the annotation’s interior color, if any.
- [PDFLineStyle.diamond](pdflinestyle/diamond.md)
  A diamond-shaped line ending filled with the annotation’s interior color, if any.
- [PDFLineStyle.openArrow](pdflinestyle/openarrow.md)
  An open arrowhead line ending, composed from two short lines meeting in an acute angle at the line end.
- [PDFLineStyle.closedArrow](pdflinestyle/closedarrow.md)
  A closed arrowhead line ending, consisting of a triangle with the acute vertex at the line end and filled with the annotation’s interior color, if any.
### Initializers
- [init?(rawValue: Int)](pdflinestyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let lineEndingStyles: PDFAnnotationKey](pdfannotationkey/lineendingstyles.md)
  An array of string values that specifies the styles to use for the ends of lines.
- [static let linePoints: PDFAnnotationKey](pdfannotationkey/linepoints.md)
  An array of floating point values that specifies the starting and ending points, in page-space coordinates, of a line.
- [struct PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdflinestyle)*