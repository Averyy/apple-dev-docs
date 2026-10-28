# PDFAnnotationStamp

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

A `PDFAnnotationStamp` object allows you to display a word or phrase, such as “Confidential,” in a PDF page.

**Availability**:
- macOS 10.5+ - Deprecated in 10.12

> **Deprecated**: Use [`PDFAnnotationSubtype`](./pdfannotationsubtype.md) instead.

## Declaration

```swift
class PDFAnnotationStamp
```

```objc
@interface PDFAnnotationStamp : PDFAnnotation
```

## Overview

A `PDFAnnotationStamp` object should have an appearance stream associated with it; otherwise, nothing useful is rendered.

## Topics

### Accessing and setting the stamp annotation
- [func name() -> String!](./pdfannotationstamp/name%28%29.md)
  Returns name associated with the stamp annotation.
- [func setName(String!)](./pdfannotationstamp/setname%28_%29.md)
  Sets the name associated with the stamp annotation.

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
- [class PDFAnnotationCircle](./pdfannotationcircle.md)
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
- [class PDFAnnotationText](./pdfannotationtext.md)
  A `PDFAnnotationText` object displays as an icon (such as a “sticky note”) attached to a specified point in the PDF document.
- [class PDFAnnotationTextWidget](./pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationstamp)*