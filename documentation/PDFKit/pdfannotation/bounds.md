# bounds

**Framework**: PDFKit  
**Kind**: property

Returns the bounding box for the annotation in page space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get set }
```

#### Return Value

The bounding box for the annotation in page space.

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [var alignment: NSTextAlignment](pdfannotation/alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var contents: String?](pdfannotation/contents.md)
  Returns the textual content (if any) associated with the annotation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/bounds)*