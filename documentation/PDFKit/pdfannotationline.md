# PDFAnnotationLine

**Framework**: PDFKit  
**Kind**: class

A `PDFAnnotationLine` object displays a single line on a page.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationLine
```

#### Overview

The [`lineWidth`](pdfborder/linewidth.md) and [`style`](pdfborder/style.md) properties of the annotation’s associated `PDFBorder` object determines the stroke thickness and style. The [`color`](pdfannotation/color.md) property of the `PDFAnnotation` class determines the stroke color.

## Topics

### Specifying the Starting and Ending Points
- [func startPoint() -> NSPoint](pdfannotationline/startpoint.md)
  Returns the starting point for the line.
- [func setStart(NSPoint)](pdfannotationline/setstart(_:)-86is0.md)
  Sets the starting point for the line.
- [func endPoint() -> NSPoint](pdfannotationline/endpoint.md)
  Returns the ending point for the line in page space.
- [func setEnd(NSPoint)](pdfannotationline/setend(_:)-2qn58.md)
  Sets the ending point for the line.
### Specifying the Line Ending Styles
- [func startLineStyle() -> PDFLineStyle](pdfannotationline/startlinestyle.md)
  Returns the line ending style for the starting point of the line.
- [func setStart(PDFLineStyle)](pdfannotationline/setstart(_:)-57pe0.md)
  Sets the line ending style for the starting point of the line.
- [func endLineStyle() -> PDFLineStyle](pdfannotationline/endlinestyle.md)
  Returns the line ending style for the ending point of the line.
- [func setEnd(PDFLineStyle)](pdfannotationline/setend(_:)-9cp0t.md)
  Sets the line ending style for the ending point of the line.
### Specifying the Color of Line-end Ornaments
- [func interiorColor() -> NSColor!](pdfannotationline/interiorcolor.md)
  Returns the color used to fill the ornament at the ends of the line.
- [func setInteriorColor(NSColor!)](pdfannotationline/setinteriorcolor(_:).md)
  Sets the color used to fill the ornament at the ends of the line.
### Constants
- [enum PDFLineStyle](pdflinestyle.md)
  The following constants specify the available line ending styles.

## Relationships

### Inherits From
- [PDFAnnotation](pdfannotation.md)
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

- [class PDFAnnotationButtonWidget](pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
- [class PDFAnnotationChoiceWidget](pdfannotationchoicewidget.md)
  A `PDFAnnotationChoiceWidget` object provides user interactivity on a page of a PDF document, in the form of pop-up menus and lists.
- [class PDFAnnotationCircle](pdfannotationcircle.md)
- [class PDFAnnotationFreeText](pdfannotationfreetext.md)
  A `PDFAnnotationFreeText` object displays text on a page.
- [class PDFAnnotationInk](pdfannotationink.md)
- [class PDFAnnotationLink](pdfannotationlink.md)
- [class PDFAnnotationMarkup](pdfannotationmarkup.md)
  A `PDFAnnotationMarkup` object appears as highlighting, underlining, or a strikethrough style applied to the text of a document.
- [class PDFAnnotationPopup](pdfannotationpopup.md)
  A `PDFAnnotationPopup` object provides user interactivity on a PDF page in the form of a pop-up menu.
- [class PDFAnnotationSquare](pdfannotationsquare.md)
  A rectangle annotation on a page.
- [class PDFAnnotationStamp](pdfannotationstamp.md)
  A `PDFAnnotationStamp` object allows you to display a word or phrase, such as “Confidential,” in a PDF page.
- [class PDFAnnotationText](pdfannotationtext.md)
  A `PDFAnnotationText` object displays as an icon (such as a “sticky note”) attached to a specified point in the PDF document.
- [class PDFAnnotationTextWidget](pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline)*