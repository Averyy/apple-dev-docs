# PDFAnnotationLineEndingStyle

**Framework**: PDFKit  
**Kind**: struct

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct PDFAnnotationLineEndingStyle
```

## Topics

### Choosing a Line-Ending Style
- [static let circle: PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle/circle.md)
  A style that displays a circle line ending and fills it with the annotation’s interior color.
- [static let closedArrow: PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle/closedarrow.md)
  A style that displays a closed arrowhead line ending and fills it with the annotation’s interior color.
- [static let diamond: PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle/diamond.md)
- [static let none: PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle/none.md)
- [static let openArrow: PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle/openarrow.md)
  A style that displays an open arrowhead line ending.
- [static let square: PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle/square.md)
  A style that displays a square line ending and fills it with the annotation’s interior color.
### Creating a Line-Ending Style
- [init(rawValue: String)](pdfannotationlineendingstyle/init(rawvalue:).md)
  Creates a line-ending style using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let lineEndingStyles: PDFAnnotationKey](pdfannotationkey/lineendingstyles.md)
  An array of string values that specifies the styles to use for the ends of lines.
- [enum PDFLineStyle](pdflinestyle.md)
  The following constants specify the available line ending styles.
- [static let linePoints: PDFAnnotationKey](pdfannotationkey/linepoints.md)
  An array of floating point values that specifies the starting and ending points, in page-space coordinates, of a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationlineendingstyle)*