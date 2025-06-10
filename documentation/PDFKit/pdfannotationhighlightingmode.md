# PDFAnnotationHighlightingMode

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
struct PDFAnnotationHighlightingMode
```

## Topics

### Choosing a Highlight Mode
- [static let invert: PDFAnnotationHighlightingMode](pdfannotationhighlightingmode/invert.md)
  A highlight mode that inverts the content of the annotation.
- [static let none: PDFAnnotationHighlightingMode](pdfannotationhighlightingmode/none.md)
  A highlight mode that doesn’t change the appearance of the annotation.
- [static let outline: PDFAnnotationHighlightingMode](pdfannotationhighlightingmode/outline.md)
  A highlight mode that inverts the annotation’s border.
- [static let push: PDFAnnotationHighlightingMode](pdfannotationhighlightingmode/push.md)
  A highlight mode that renders a pressed appearance for the annotation.
### Creating an Annotation Highlight Mode
- [init(rawValue: String)](pdfannotationhighlightingmode/init(rawvalue:).md)
  Creates a highlight mode using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let appearanceDictionary: PDFAnnotationKey](pdfannotationkey/appearancedictionary.md)
  A dictionary that contains properties for controlling the annotation’s visual appearance.
- [static let appearanceState: PDFAnnotationKey](pdfannotationkey/appearancestate.md)
  A string that specifies the appearance stream for the annotation.
- [static let border: PDFAnnotationKey](pdfannotationkey/border.md)
  An array of integers or border objects that describes the border of the annotation.
- [static let borderStyle: PDFAnnotationKey](pdfannotationkey/borderstyle.md)
  A dictionary that contains the properties of the annotation’s border.
- [static let color: PDFAnnotationKey](pdfannotationkey/color.md)
  An array of floats or a color object that specifies the annotation’s color.
- [static let defaultAppearance: PDFAnnotationKey](pdfannotationkey/defaultappearance.md)
  A string value a free text annotation uses to format the text.
- [static let highlightingMode: PDFAnnotationKey](pdfannotationkey/highlightingmode.md)
  A string value that defines the way an annotation highlights when the user activates it, such as when clicking or tapping a link.
- [static let iconName: PDFAnnotationKey](pdfannotationkey/iconname.md)
  A string value that specifies the name of an icon for a text or stamp annotation.
- [static let interiorColor: PDFAnnotationKey](pdfannotationkey/interiorcolor.md)
  An array of floating point values or a PDF color object that annotations use to fill interior space, such as line endings, squares, or circles.
- [static let quadding: PDFAnnotationKey](pdfannotationkey/quadding.md)
  An integer value that specifies left, right, or center justification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationhighlightingmode)*