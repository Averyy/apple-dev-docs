# PDFAnnotationCircle

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

> **Deprecated**: Use [`PDFAnnotationSubtype`](./pdfannotationsubtype.md) instead.

## Declaration

```swift
class PDFAnnotationCircle
```

```objc
@interface PDFAnnotationCircle : PDFAnnotation
```

#### Overview

A PDFAnnotationCircle object displays an ellipse on a page. Circle annotations are like square annotations (instances of the PDFAnnotationSquare class) apart from the shape.

The [`lineWidth`](./pdfborder/linewidth.md) and [`style`](./pdfborder/style.md) properties of the annotation’s associated `PDFBorder` object determines the stroke thickness and style. The [`color`](./pdfannotation/color.md) property of the `PDFAnnotation` class determines the stroke color.

## Topics

### Accessor methods
- [func interiorColor() -> NSColor!](./pdfannotationcircle/interiorcolor%28%29.md)
  Returns the fill color used for drawing the annotation.
- [func setInteriorColor(NSColor!)](./pdfannotationcircle/setinteriorcolor%28_%29.md)
  Sets the fill color used for drawing the annotation.

## Relationships

### Inherits From
- [PDFAnnotation](./pdfannotation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated Annotation Types
- [class PDFAnnotationButtonWidget](./pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
- [class PDFAnnotationChoiceWidget](./pdfannotationchoicewidget.md)
  A `PDFAnnotationChoiceWidget` object provides user interactivity on a page of a PDF document, in the form of pop-up menus and lists.
- [class PDFAnnotationFreeText](./pdfannotationfreetext.md)
  A `PDFAnnotationFreeText` object displays text on a page.
- [class PDFAnnotationInk](./pdfannotationink.md)
- [class PDFAnnotationLine](./pdfannotationline.md)
  A `PDFAnnotationLine` object displays a single line on a page.
- [class PDFAnnotationLink](./pdfannotationlink.md)
- [class PDFAnnotationMarkup](./pdfannotationmarkup.md)
  A `PDFAnnotationMarkup` object appears as highlighting, underlining, or a strikethrough style applied to the text of a document.
- [class PDFAnnotationPopup](./pdfannotationpopup.md)
  A `PDFAnnotationPopup` object provides user interactivity on a PDF page in the form of a pop-up menu.
- [class PDFAnnotationSquare](./pdfannotationsquare.md)
  A rectangle annotation on a page.
- [class PDFAnnotationStamp](./pdfannotationstamp.md)
  A `PDFAnnotationStamp` object allows you to display a word or phrase, such as “Confidential,” in a PDF page.
- [class PDFAnnotationText](./pdfannotationtext.md)
  A `PDFAnnotationText` object displays as an icon (such as a “sticky note”) attached to a specified point in the PDF document.
- [class PDFAnnotationTextWidget](./pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationcircle)*