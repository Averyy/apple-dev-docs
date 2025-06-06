# PDFBorder

**Framework**: PDFKit  
**Kind**: class

An optional border for an annotation that lies completely within the annotation rectangle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFBorder
```

## Topics

### Working with Border Styles and Characteristics
- [var style: PDFBorderStyle](pdfborder/style.md)
  Sets the border style.
- [enum PDFBorderStyle](pdfborderstyle.md)
  PDF Kit annotation borders may have the following styles.
- [var lineWidth: CGFloat](pdfborder/linewidth.md)
  Sets the line width (in points) for the border.
- [var dashPattern: [Any]?](pdfborder/dashpattern.md)
  Gets the dash pattern for the border as an array of NSNumber objects.
- [var borderKeyValues: [AnyHashable : Any]](pdfborder/borderkeyvalues.md)
  A dictionary that contains a deep copy of all border properties.
- [struct PDFBorderKey](pdfborderkey.md)
### Drawing Borders
- [func draw(in: CGRect)](pdfborder/draw(in:).md)
  Draws the border.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [var isHighlighted: Bool](pdfannotation/ishighlighted.md)
  A Boolean value that indicates whether the annotation is in a highlighted state, such as when the mouse is down on a link annotation.
- [var color: UIColor](pdfannotation/color.md)
  Sets the stroke color for the annotation.
- [var hasAppearanceStream: Bool](pdfannotation/hasappearancestream.md)
  Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfborder)*