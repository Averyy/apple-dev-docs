# PDFAnnotationInk

**Framework**: PDFKit  
**Kind**: class

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationInk
```

#### Overview

A `PDFAnnotationInk` object displays one or more disjoint Bezier paths on a page. This is typically used to represent a freehand jotting or “scribble” of handwritten text.

The [`lineWidth`](pdfborder/linewidth.md) and [`style`](pdfborder/style.md) properties of the annotation’s associated `PDFBorder` object determines the stroke thickness and style. The [`color`](pdfannotation/color.md) property of the `PDFAnnotation` class determines the stroke color.

## Topics

### Accessor methods
- [func paths() -> [Any]!](pdfannotationink/paths.md)
  Returns an array containing the Bezier paths that make up an annotation.
### Working with Bezier paths
- [func add(NSBezierPath!)](pdfannotationink/add(_:).md)
  Adds a Bezier path to an annotation.
- [func remove(NSBezierPath!)](pdfannotationink/remove(_:).md)
  Removes a Bezier path from an annotation.

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
- [class PDFAnnotationLine](pdfannotationline.md)
  A `PDFAnnotationLine` object displays a single line on a page.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationink)*