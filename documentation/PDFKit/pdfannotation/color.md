# color

**Framework**: PDFKit  
**Kind**: property

Sets the stroke color for the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var color: NSColor { get set }
```

#### Discussion

Where this color is used depends on the annotation type.

## Parameters

- `color`: The stroke color for the annotation.

## See Also

- [var alignment: NSTextAlignment](pdfannotation/alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var bounds: CGRect](pdfannotation/bounds.md)
  Returns the bounding box for the annotation in page space.
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
- [var hasAppearanceStream: Bool](pdfannotation/hasappearancestream.md)
  Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/color)*