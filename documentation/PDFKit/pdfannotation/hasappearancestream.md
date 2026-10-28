# hasAppearanceStream

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var hasAppearanceStream: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasAppearanceStream;
```

## Mentions

- [Adding Custom Graphics to a PDF](../adding-custom-graphics-to-a-pdf.md)

## Return Value

[`true`](../../Swift/true.md) if the annotation has an appearance stream; otherwise [`false`](../../Swift/false.md).

## Discussion

An appearance stream is a sequence of draw instructions used to render a PDF item. If an appearance stream exists, PDF Kit draws the annotation using the stream, which may override existing set parameters (such as the stroke color set with `setColor`).

## See Also

### Managing Annotation Display Characteristics
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var bounds: CGRect](./bounds.md)
  Returns the bounding box for the annotation in page space.
- [var contents: String?](./contents.md)
  Returns the textual content (if any) associated with the annotation.
- [var font: UIFont?](./font.md)
  The font the annotation uses to display text.
- [var fontColor: UIColor?](./fontcolor.md)
  The font color the annotation uses to display text.
- [var border: PDFBorder?](./border.md)
  Sets the border style for the annotation.
- [class PDFBorder](../pdfborder.md)
  An optional border for an annotation that lies completely within the annotation rectangle.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the annotation is in a highlighted state, such as when the mouse is down on a link annotation.
- [var color: UIColor](./color.md)
  Sets the stroke color for the annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/hasappearancestream)*