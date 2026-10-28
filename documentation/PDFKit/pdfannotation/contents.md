# contents

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSString * contents;
```

## Return Value

A string representing the textual content associated with the annotation.

## Discussion

Textual content is typically associated with `PDFAnnotationText` and `PDFAnnotationFreeText` annotations.

## See Also

### Related Documentation
- [var toolTip: String?](./tooltip.md)
  Returns text for display as a help tag.
### Managing Annotation Display Characteristics
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var bounds: CGRect](./bounds.md)
  Returns the bounding box for the annotation in page space.
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
- [var hasAppearanceStream: Bool](./hasappearancestream.md)
  Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/contents)*