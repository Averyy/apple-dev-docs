# PDFAnnotationChoiceWidget

**Framework**: PDFKit  
**Kind**: class

A `PDFAnnotationChoiceWidget` object provides user interactivity on a page of a PDF document, in the form of pop-up menus and lists.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationChoiceWidget
```

#### Overview

`PDFAnnotationChoiceWidget` inherits general annotation behavior from the `PDFAnnotation` class. If you use a `PDFAnnotationChoiceWidget` object, your application must handle hit testing, unless you are simply using `PDFView` to display content. This is because `PDFView` automatically handles hit testing for you.

## Topics

### Getting and Setting the String Value
- [func stringValue() -> String!](pdfannotationchoicewidget/stringvalue.md)
  Returns the selection in the widget annotation.
- [func setStringValue(String!)](pdfannotationchoicewidget/setstringvalue(_:).md)
  Sets the selection in the widget annotation.
### Managing Font and Background Color Characteristics
- [func backgroundColor() -> NSColor!](pdfannotationchoicewidget/backgroundcolor.md)
  Returns the color of the widget annotation background.
- [func setBackgroundColor(NSColor!)](pdfannotationchoicewidget/setbackgroundcolor(_:).md)
  Sets the background color of the widget annotation.
- [func font() -> NSFont!](pdfannotationchoicewidget/font.md)
  Returns the font used to display the text in the widget annotation.
- [func setFont(NSFont!)](pdfannotationchoicewidget/setfont(_:).md)
  Sets the font used to display the text in the widget annotation.
- [func fontColor() -> NSColor!](pdfannotationchoicewidget/fontcolor.md)
  Returns the font color used to display the text in the widget annotation.
- [func setFontColor(NSColor!)](pdfannotationchoicewidget/setfontcolor(_:).md)
  Sets the font color used to display the text in the widget annotation.
### Managing the Associated Field Name
- [func fieldName() -> String!](pdfannotationchoicewidget/fieldname.md)
  Returns the internal field name associated with the widget annotation.
- [func setFieldName(String!)](pdfannotationchoicewidget/setfieldname(_:).md)
  Sets the internal field name associated with the widget annotation’s value.
### Determining the Type of Choice Widget Annotation
- [func isListChoice() -> Bool](pdfannotationchoicewidget/islistchoice.md)
  Returns a Boolean value indicating whether the widget annotation is a list.
- [func setIsListChoice(Bool)](pdfannotationchoicewidget/setislistchoice(_:).md)
  Sets whether the widget annotation is a list.
### Accessing the Items in the Choice Widget Annotation
- [func choices() -> [Any]!](pdfannotationchoicewidget/choices.md)
  Returns an array of strings that represent the items available in the list or pop-up menu of the choice widget annotation.
- [func setChoices([Any]!)](pdfannotationchoicewidget/setchoices(_:).md)
  Sets the items available in the list or pop-up menu of the choice widget annotation.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget)*