# bounds

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the bounding box for the annotation in page space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var bounds: CGRect { get set }
```

*macOS*

```swift
var bounds: NSRect { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic) CGRect bounds;
```

*macOS*

```objc
@property (nonatomic) NSRect bounds;
```

## Return Value

The bounding box for the annotation in page space.

## Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Managing Annotation Display Characteristics
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment of the free text and text widget annotation’s text content.
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
- [var hasAppearanceStream: Bool](./hasappearancestream.md)
  Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/bounds)*