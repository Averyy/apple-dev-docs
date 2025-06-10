# PDFAnnotationSubtype

**Framework**: PDFKit  
**Kind**: struct

The type of annotation, such as circle, text, or ink.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct PDFAnnotationSubtype
```

## Topics

### Choosing an Annotation Subtype
- [static let circle: PDFAnnotationSubtype](pdfannotationsubtype/circle.md)
  An annotation that renders a circle shape.
- [static let freeText: PDFAnnotationSubtype](pdfannotationsubtype/freetext.md)
  An annotation that displays an editable text field.
- [static let highlight: PDFAnnotationSubtype](pdfannotationsubtype/highlight.md)
  An annotation that highlights text.
- [static let ink: PDFAnnotationSubtype](pdfannotationsubtype/ink.md)
  An annotation that represents a freehand scribble.
- [static let line: PDFAnnotationSubtype](pdfannotationsubtype/line.md)
  An annotation that displays a single straight line.
- [static let link: PDFAnnotationSubtype](pdfannotationsubtype/link.md)
  An annotation that provides a hyperlink to a location in the document, or an action to perform when the user clicks or taps it.
- [static let popup: PDFAnnotationSubtype](pdfannotationsubtype/popup.md)
  An annotation that displays text in a pop-up window for entry and editing.
- [static let square: PDFAnnotationSubtype](pdfannotationsubtype/square.md)
  An annotation that displays a square shape.
- [static let stamp: PDFAnnotationSubtype](pdfannotationsubtype/stamp.md)
  An annotation that displays text or a graphic as if a rubber stamp imprints it on the page.
- [static let strikeOut: PDFAnnotationSubtype](pdfannotationsubtype/strikeout.md)
  An annotation that strikes out text.
- [static let text: PDFAnnotationSubtype](pdfannotationsubtype/text.md)
  An annotation that displays a collapsible note that contains text.
- [static let underline: PDFAnnotationSubtype](pdfannotationsubtype/underline.md)
  An annotation that underlines text.
- [static let widget: PDFAnnotationSubtype](pdfannotationsubtype/widget.md)
  An annotation that displays interactive form elements, including text or signature fields, radio buttons, checkboxes, push buttons, pop-ups, and tables.
### Creating an Annotation Subtype
- [init(rawValue: String)](pdfannotationsubtype/init(rawvalue:).md)
  Creates an annotation subtype using the specified raw string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(bounds: CGRect, forType: PDFAnnotationSubtype, withProperties: [AnyHashable : Any]?)](pdfannotation/init(bounds:fortype:withproperties:).md)
  Creates a PDF annotation with the specified bounds, type, and optional properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationsubtype)*