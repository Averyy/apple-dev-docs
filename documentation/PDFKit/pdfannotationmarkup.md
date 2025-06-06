# PDFAnnotationMarkup

**Framework**: PDFKit  
**Kind**: class

A `PDFAnnotationMarkup` object appears as highlighting, underlining, or a strikethrough style applied to the text of a document.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationMarkup
```

#### Overview

The [`lineWidth`](pdfborder/linewidth.md) and [`style`](pdfborder/style.md) properties of the annotation’s associated `PDFBorder` object determines the stroke thickness and style. The [`color`](pdfannotation/color.md) property of the `PDFAnnotation` class determines the stroke color.

## Topics

### Working with Markup Boundaries
- [func quadrilateralPoints() -> [Any]!](pdfannotationmarkup/quadrilateralpoints.md)
  Gets the array of quadrilateral points defining the bounds of the markup.
- [func setQuadrilateralPoints([Any]!)](pdfannotationmarkup/setquadrilateralpoints(_:).md)
  Sets the array of quadrilateral points defining the bounds of the markup.
### Working with Markup Style
- [func markupType() -> PDFMarkupType](pdfannotationmarkup/markuptype.md)
  Gets the markup style.
- [func setMarkupType(PDFMarkupType)](pdfannotationmarkup/setmarkuptype(_:).md)
  Sets the markup style.
### Constants
- [enum PDFMarkupType](pdfmarkuptype.md)
  The styles available for markup annotations in PDFKit.

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
- [class PDFAnnotationLine](pdfannotationline.md)
  A `PDFAnnotationLine` object displays a single line on a page.
- [class PDFAnnotationLink](pdfannotationlink.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationmarkup)*