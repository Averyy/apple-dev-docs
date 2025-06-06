# contents

**Framework**: PDFKit  
**Kind**: property

Returns the textual content (if any) associated with the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var contents: String? { get set }
```

#### Return Value

A string representing the textual content associated with the annotation.

#### Discussion

Textual content is typically associated with `PDFAnnotationText` and `PDFAnnotationFreeText` annotations.

## See Also

- [var toolTip: String?](pdfannotation/tooltip.md)
  Returns text for display as a help tag.
- [var alignment: NSTextAlignment](pdfannotation/alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var bounds: CGRect](pdfannotation/bounds.md)
  Returns the bounding box for the annotation in page space.
- [var font: UIFont?](pdfannotation/font.md)
  The font the annotation uses to display text.
- [var fontColor: UIColor?](pdfannotation/fontcolor.md)
  The font color the annotation uses to display text.
- [var border: PDFBorder?](pdfannotation/border.md)
  Sets the border style for the annotation.
- [class PDFBorder](pdfborder.md)
  An optional border for an annotation that lies completely within the annotation rectangle.
- [var isHighlighted: Bool](pdfannotation/ishighlighted.md)
  A Boolean value that indicates whether the annotation is in a highlighted state, such as when the mouse is down on a link annotation.
- [var color: UIColor](pdfannotation/color.md)
  Sets the stroke color for the annotation.
- [var hasAppearanceStream: Bool](pdfannotation/hasappearancestream.md)
  Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/contents)*