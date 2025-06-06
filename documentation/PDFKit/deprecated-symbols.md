# Deprecated Symbols

**Framework**: PDFKit

Review unsupported symbols and their replacements.

## Topics

### Deprecated Annotation Types
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
### Deprecated Methods
- [convenience init(bounds: NSRect)](pdfannotation/init(bounds:).md)
  Creates a PDF annotation object.
- [convenience init(dictionary: [AnyHashable : Any], forPage: PDFPage?)](pdfannotation/init(dictionary:forpage:).md)
- [func removeAllAppearanceStreams()](pdfannotation/removeallappearancestreams.md)
- [func draw(with: PDFDisplayBox)](pdfannotation/draw(with:).md)
  Draws the annotation on its associated page.
### Deprecated Properties
- [var mouseUpAction: PDFAction?](pdfannotation/mouseupaction.md)
  The action to perform when a user releases the mouse button within an annotation.
- [var toolTip: String?](pdfannotation/tooltip.md)
  Returns text for display as a help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/deprecated-symbols)*