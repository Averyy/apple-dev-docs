# PDFAnnotationFreeText

**Framework**: PDFKit  
**Kind**: class

A `PDFAnnotationFreeText` object displays text on a page.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationFreeText
```

#### Overview

Unlike a `PDFAnnotationText` object, a `PDFAnnotationFreeText` object has no open or closed state; its text is always visible. The text annotation performed in Preview uses `PDFAnnotationFreeText`.

The `PDFAnnotation` class’s [`contents`](pdfannotation/contents.md) property lets you get and set the textual content for a `PDFAnnotationFreeText` object.

## Topics

### Managing Text Alignment
- [func alignment() -> NSTextAlignment](pdfannotationfreetext/alignment.md)
  Returns the horizontal alignment of text within the bounds of the annotation.
- [func setAlignment(NSTextAlignment)](pdfannotationfreetext/setalignment(_:).md)
  Sets the horizontal alignment of text within the bounds of the annotation.
### Managing Font and Font Color
- [func font() -> NSFont!](pdfannotationfreetext/font.md)
  Returns the font used for the annotation’s text field.
- [func setFont(NSFont!)](pdfannotationfreetext/setfont(_:).md)
  Sets the font used in the text field of the annotation.
- [func fontColor() -> NSColor!](pdfannotationfreetext/fontcolor.md)
  Returns the font color used in the text field of the annotation.
- [func setFontColor(NSColor!)](pdfannotationfreetext/setfontcolor(_:).md)
  Sets the font color used in the text field of the annotation.

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
- [class PDFAnnotationInk](pdfannotationink.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationfreetext)*