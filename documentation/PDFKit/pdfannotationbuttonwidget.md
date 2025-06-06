# PDFAnnotationButtonWidget

**Framework**: PDFKit  
**Kind**: class

A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class PDFAnnotationButtonWidget
```

#### Overview

`PDFAnnotationButtonWidget` inherits general annotation behavior from the `PDFAnnotation` class. If you use a `PDFAnnotationButtonWidget` object, your application must handle hit testing, unless you are simply using `PDFView` to display content. This is because `PDFView` automatically handles hit testing for you.

## Topics

### Getting and Setting the Control Type
- [func controlType() -> PDFWidgetControlType](pdfannotationbuttonwidget/controltype.md)
  Returns the type of the control.
- [func setControlType(PDFWidgetControlType)](pdfannotationbuttonwidget/setcontroltype(_:).md)
  Sets the type of the control.
### Getting and Setting the Control’s State
- [func state() -> Int](pdfannotationbuttonwidget/state.md)
  Returns the state of the control.
- [func setState(Int)](pdfannotationbuttonwidget/setstate(_:).md)
  Sets the state of the control.
### Getting and Setting the Control’s Appearance
- [func backgroundColor() -> NSColor!](pdfannotationbuttonwidget/backgroundcolor.md)
  Returns the background color of the control.
- [func setBackgroundColor(NSColor!)](pdfannotationbuttonwidget/setbackgroundcolor(_:).md)
  Sets the control’s background color.
### Getting and Setting the Control Label Font Attributes
- [func font() -> NSFont!](pdfannotationbuttonwidget/font.md)
  Returns the font used in the control’s label.
- [func setFont(NSFont!)](pdfannotationbuttonwidget/setfont(_:).md)
  Sets the font of the control’s label.
- [func fontColor() -> NSColor!](pdfannotationbuttonwidget/fontcolor.md)
  Returns the font color used in the control’s label.
- [func setFontColor(NSColor!)](pdfannotationbuttonwidget/setfontcolor(_:).md)
  Sets the font color used in the control’s label.
### Getting and Setting the Control Label Text
- [func caption() -> String!](pdfannotationbuttonwidget/caption.md)
  Returns the text of the label on a push button control.
- [func setCaption(String!)](pdfannotationbuttonwidget/setcaption(_:).md)
  Sets the text of the label on a push button control.
### Managing Radio Button Behavior
- [func allowsToggleToOff() -> Bool](pdfannotationbuttonwidget/allowstoggletooff.md)
  Returns a Boolean value indicating whether a radio button behaves in a toggling manner.
### Managing Control State Values and Form Fields
- [func onStateValue() -> String!](pdfannotationbuttonwidget/onstatevalue.md)
  Returns the string associated with the on state of a radio button or checkbox control.
- [func setOnStateValue(String!)](pdfannotationbuttonwidget/setonstatevalue(_:).md)
  Sets the string that is associated with the on state of a radio button or checkbox control.
- [func fieldName() -> String!](pdfannotationbuttonwidget/fieldname.md)
  Returns the internal name of a field (used for reset-form actions).
- [func setFieldName(String!)](pdfannotationbuttonwidget/setfieldname(_:).md)
  Sets the internal name of a field (used for reset-form actions).
### Constants
- [enum PDFWidgetControlType](pdfwidgetcontroltype.md)
  The types of annotation buttons.
### Instance Methods
- [func setAllowsToggleToOff(Bool)](pdfannotationbuttonwidget/setallowstoggletooff(_:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget)*