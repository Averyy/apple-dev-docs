# PDFAnnotationTextWidget

**Framework**: PDFKit  
**Kind**: class

A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationTextWidget
```

#### Overview

`PDFAnnotationTextWidget` objects support interactive forms in a PDF document. This object is comparable to an editable `NSTextField` in Cocoa or an edit text view in Carbon.

## Topics

### Working with Annotation Strings
- [func stringValue() -> String!](pdfannotationtextwidget/stringvalue.md)
  Returns the string assigned to the annotation.
- [func setStringValue(String!)](pdfannotationtextwidget/setstringvalue(_:).md)
  Sets the string for the annotation.
- [func maximumLength() -> Int](pdfannotationtextwidget/maximumlength.md)
  Returns the maximum number of characters allowed in the annotation string.
- [func setMaximumLength(Int)](pdfannotationtextwidget/setmaximumlength(_:).md)
  Sets the maximum number of characters allowed in the annotation string.
### Managing the Font and Font Color
- [func font() -> NSFont!](pdfannotationtextwidget/font.md)
  Returns the font used for the annotation’s text field.
- [func setFont(NSFont!)](pdfannotationtextwidget/setfont(_:).md)
  Sets the font used in the text field of the annotation.
- [func fontColor() -> NSColor!](pdfannotationtextwidget/fontcolor.md)
  Returns the font color used for the annotation’s text field.
- [func setFontColor(NSColor!)](pdfannotationtextwidget/setfontcolor(_:).md)
  Sets the font color used for the annotation’s text field.
### Managing Background Color, Alignment, and Rotation
- [func backgroundColor() -> NSColor!](pdfannotationtextwidget/backgroundcolor.md)
  Returns the background color of the annotation text field.
- [func setBackgroundColor(NSColor!)](pdfannotationtextwidget/setbackgroundcolor(_:).md)
  Sets the background color of the annotation text field.
- [func alignment() -> NSTextAlignment](pdfannotationtextwidget/alignment.md)
  Returns the text alignment setting for the annotation.
- [func setAlignment(NSTextAlignment)](pdfannotationtextwidget/setalignment(_:).md)
  Sets the text alignment for the annotation.
- [func rotation() -> Int](pdfannotationtextwidget/rotation.md)
  Returns the rotation angle of the annotation text field in degrees.
- [func setRotation(Int32)](pdfannotationtextwidget/setrotation(_:).md)
  Sets the rotation angle of the annotation text field in degrees.
### Working with Field Names
- [func fieldName() -> String!](pdfannotationtextwidget/fieldname.md)
  Returns the internal name for the annotation text field.
- [func setFieldName(String!)](pdfannotationtextwidget/setfieldname(_:).md)
  Sets the internal field name for the annotation text field.
### Instance Methods
- [func attributedStringValue() -> NSAttributedString!](pdfannotationtextwidget/attributedstringvalue.md)
- [func isMultiline() -> Bool](pdfannotationtextwidget/ismultiline.md)
- [func setAttributedStringValue(NSAttributedString!)](pdfannotationtextwidget/setattributedstringvalue(_:).md)
- [func setIsMultiline(Bool)](pdfannotationtextwidget/setismultiline(_:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget)*