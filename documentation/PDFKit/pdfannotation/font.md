# font

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The font the annotation uses to display text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
@NSCopying
var font: UIFont? { get set }
```

*macOS*

```swift
@NSCopying
var font: NSFont? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) UIFont * font;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSFont * font;
```

## Mentions

- [Adding Widgets to a PDF Document](../adding-widgets-to-a-pdf-document.md)

## See Also

### Managing Annotation Display Characteristics
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var bounds: CGRect](./bounds.md)
  Returns the bounding box for the annotation in page space.
- [var contents: String?](./contents.md)
  Returns the textual content (if any) associated with the annotation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/font)*