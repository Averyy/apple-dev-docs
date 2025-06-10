# PDFAnnotation

**Framework**: PDFKit  
**Kind**: class

An annotation in a PDF document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFAnnotation
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)
- [Adding Widgets to a PDF Document](adding-widgets-to-a-pdf-document.md)

#### Overview

In addition to its primary textual content, a PDF file can contain annotations that represent links, form elements, highlighting circles, textual notes, and so on. Each annotation has a specific location on a page and may offer interactivity with the user.

## Topics

### Creating an Annotation
- [init(bounds: CGRect, forType: PDFAnnotationSubtype, withProperties: [AnyHashable : Any]?)](pdfannotation/init(bounds:fortype:withproperties:).md)
  Creates a PDF annotation with the specified bounds, type, and optional properties.
- [struct PDFAnnotationSubtype](pdfannotationsubtype.md)
  The type of annotation, such as circle, text, or ink.
### Accessing Information About an Annotation
- [var page: PDFPage?](pdfannotation/page.md)
  Returns the page that the annotation is associated with.
- [var modificationDate: Date?](pdfannotation/modificationdate.md)
  Returns the modification date of the annotation.
- [var userName: String?](pdfannotation/username.md)
  Returns the name of the user who created the annotation.
- [var type: String?](pdfannotation/type.md)
  Returns the type of the annotation.
- [var action: PDFAction?](pdfannotation/action.md)
  An object that represents an action for a PDF element, such as a link annotation.
- [class PDFAction](pdfaction.md)
  An action that is performed when, for example, a PDF annotation is activated or an outline item is clicked.
- [class PDFDestination](pdfdestination.md)
  A `PDFDestination` object describes a point on a PDF page.
### Managing Annotation Drawing and Output
- [func draw(with: PDFDisplayBox, in: CGContext)](pdfannotation/draw(with:in:).md)
  Draws the annotation in a graphics context using page-space coordinates relative to the origin of the specified box.
- [var shouldDisplay: Bool](pdfannotation/shoulddisplay.md)
  Returns a Boolean value indicating whether the annotation should be displayed.
- [var shouldPrint: Bool](pdfannotation/shouldprint.md)
  Returns a Boolean value indicating whether the annotation should appear when the document is printed.
### Modifying Annotation Attributes
- [var annotationKeyValues: [AnyHashable : Any]](pdfannotation/annotationkeyvalues.md)
  A dictionary that contains a deep copy of the widget’s properties.
- [func value(forAnnotationKey: PDFAnnotationKey) -> Any?](pdfannotation/value(forannotationkey:).md)
  Returns a deep copy of the key-value pairs of properties for the specified key.
- [func setValue(Any, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setvalue(_:forannotationkey:).md)
  Sets a value in the annotation’s dictionary.
- [func setBoolean(Bool, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setboolean(_:forannotationkey:).md)
  Sets a Boolean value in the annotation’s dictionary.
- [func setRect(CGRect, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setrect(_:forannotationkey:).md)
  Sets a rectangle value in the annotation’s dictionary.
- [func removeValue(forAnnotationKey: PDFAnnotationKey)](pdfannotation/removevalue(forannotationkey:).md)
  Removes a value from the annotation’s dictionary.
- [struct PDFAnnotationKey](pdfannotationkey.md)
  Keys for setting properties of annotations.
### Managing Annotation Display Characteristics
- [var alignment: NSTextAlignment](pdfannotation/alignment.md)
  The alignment of the free text and text widget annotation’s text content.
- [var bounds: CGRect](pdfannotation/bounds.md)
  Returns the bounding box for the annotation in page space.
- [var contents: String?](pdfannotation/contents.md)
  Returns the textual content (if any) associated with the annotation.
- [var font: UIFont?](pdfannotation/font.md)
  The font the annotation uses to display text.
- [var fontColor: UIColor?](pdfannotation/fontcolor.md)
  The font color the annotation uses to display text.
- [var border: PDFBorder?](pdfannotation/border.md)
  Sets the border style for the annotation.
- [class PDFBorder](pdfborder.md)
  An optional border for an annotation that lies completely within the annotation rectangle.
- [var isHighlighted: Bool](pdfannotation/ishighlighted.md)
  A Boolean value that indicates whether the annotation is in a highlighted state, such as when the mouse is down on a link annotation.
- [var color: UIColor](pdfannotation/color.md)
  Sets the stroke color for the annotation.
- [var hasAppearanceStream: Bool](pdfannotation/hasappearancestream.md)
  Returns a Boolean value that indicates whether the annotation has an appearance stream associated with it.
### Configuring Shape Annotations
- [var interiorColor: UIColor?](pdfannotation/interiorcolor.md)
  The fill color for drawing a circle, line, or square annotation.
### Configuring Line Annotations
- [var startPoint: CGPoint](pdfannotation/startpoint.md)
  The point where a line begins, in annotation-space coordinates.
- [var endPoint: CGPoint](pdfannotation/endpoint.md)
  The point where a line ends, in annotation-space coordinates.
- [var startLineStyle: PDFLineStyle](pdfannotation/startlinestyle.md)
  The style of the line annotation’s starting point, such as square or filled arrowhead.
- [var endLineStyle: PDFLineStyle](pdfannotation/endlinestyle.md)
  The style of the line annotation’s ending point, such as square or filled arrowhead.
- [class func lineStyle(fromName: String) -> PDFLineStyle](pdfannotation/linestyle(fromname:).md)
  Returns a line style that corresponds to the specified name.
- [class func name(for: PDFLineStyle) -> String](pdfannotation/name(for:).md)
  Returns the name of the line style, which matches the definition in the Adobe PDF Specification.
### Configuring Link Annotations
- [var destination: PDFDestination?](pdfannotation/destination.md)
  The destination for a link annotation.
- [var url: URL?](pdfannotation/url.md)
  A URL for a link annotation.
### Configuring Text Annotations
- [var iconType: PDFTextAnnotationIconType](pdfannotation/icontype.md)
  The type of icon to display for a pop-up text annotation.
- [enum PDFTextAnnotationIconType](pdftextannotationicontype.md)
  The types of icons that a text annotation can use.
- [struct PDFAnnotationTextIconType](pdfannotationtexticontype.md)
  Constants for icon type values in text annotation property dictionaries.
### Configuring Pop-Up Annotations
- [var popup: PDFAnnotation?](pdfannotation/popup.md)
  Returns the pop-up annotation associated with an annotation.
- [var isOpen: Bool](pdfannotation/isopen.md)
  A Boolean value that indicates whether the pop-up annotation is in an opened state, displaying its text content, or in a closed state, displaying an icon.
### Configuring Text Markup Annotations
- [var markupType: PDFMarkupType](pdfannotation/markuptype.md)
  The markup type that the annotation displays, either highlight, strikethrough, underline, or redact.
- [enum PDFMarkupType](pdfmarkuptype.md)
  The styles available for markup annotations in PDFKit.
- [var quadrilateralPoints: [NSValue]?](pdfannotation/quadrilateralpoints.md)
  An array of values that represents the points bounding the marked-up text.
### Configuring Widget Annotations
- [var widgetFieldType: PDFAnnotationWidgetSubtype](pdfannotation/widgetfieldtype.md)
  The type of widget annotation, such as button, choice, or text.
- [var widgetStringValue: String?](pdfannotation/widgetstringvalue.md)
  The string value of the widget annotation.
- [var widgetDefaultStringValue: String?](pdfannotation/widgetdefaultstringvalue.md)
  The string value that the widget reverts to when performing a reset form action.
- [var fieldName: String?](pdfannotation/fieldname.md)
  The widget identifier for form annotation actions and behaviors.
- [var backgroundColor: UIColor?](pdfannotation/backgroundcolor.md)
  The color of the widget’s background.
- [var isReadOnly: Bool](pdfannotation/isreadonly.md)
  A Boolean value that determines whether the widget is editable.
- [enum PDFWidgetControlType](pdfwidgetcontroltype.md)
  The types of annotation buttons.
- [class PDFAppearanceCharacteristics](pdfappearancecharacteristics.md)
  An object that represents appearance characteristics of a widget annotation.
### Configuring Text Widget Annotations
- [var isMultiline: Bool](pdfannotation/ismultiline.md)
  A Boolean value that indicates whether the text widget annotation displays multiple lines.
- [var isPasswordField: Bool](pdfannotation/ispasswordfield.md)
  A Boolean value that indicates whether the text widget annotation displays a password field using bullet characters.
- [var maximumLength: Int](pdfannotation/maximumlength.md)
  The maximum number of characters the text widget annotation allows.
- [var hasComb: Bool](pdfannotation/hascomb.md)
  A Boolean value that indicates whether the annotation divides the text widget’s bounds into equally spaced segments, such as in a form entry field.
### Configuring Button Widget Annotations
- [var widgetControlType: PDFWidgetControlType](pdfannotation/widgetcontroltype.md)
  The type of button widget control, either radio button, push button, or checkbox.
- [var buttonWidgetState: PDFWidgetCellState](pdfannotation/buttonwidgetstate.md)
  The current state of the button widget annotation.
- [enum PDFWidgetCellState](pdfwidgetcellstate.md)
  The state of a button annotation, either on, off, or mixed.
- [var buttonWidgetStateString: String](pdfannotation/buttonwidgetstatestring.md)
  A string value that differentiates button widgets in the same group, such as to identify mutually exclusive radio buttons from each other.
- [var caption: String?](pdfannotation/caption.md)
  The title of push button widget annotations.
- [var allowsToggleToOff: Bool](pdfannotation/allowstoggletooff.md)
  A Boolean value that indicates whether clicking or tapping a selected radio button toggles it to an unselected state.
- [var radiosInUnison: Bool](pdfannotation/radiosinunison.md)
  A Boolean value that indicates whether radio buttons in a group turn on and off in unison.
### Configuring Choice Widget Annotations
- [var choices: [String]?](pdfannotation/choices.md)
  An array of strings that specifies the options in either a list or a pop-up menu.
- [var isListChoice: Bool](pdfannotation/islistchoice.md)
  A Boolean value that indicates whether the choice widget annotation is a list or a pop-up menu.
- [var values: [String]?](pdfannotation/values.md)
  An array of strings that specifies the export values for items in a list or a pop-up menu.
### Configuring Ink Annotations
- [var paths: [UIBezierPath]?](pdfannotation/paths.md)
  An array of bezier paths, in annotation-space coordinates, that compose the annotation.
- [func add(UIBezierPath)](pdfannotation/add(_:).md)
  Adds a bezier path to the ink annotation.
- [func remove(UIBezierPath)](pdfannotation/remove(_:).md)
  Removes a bezier path from an ink annotation.
### Configuring Stamp Annotations
- [var stampName: String?](pdfannotation/stampname.md)
  The name of the stamp, a text or graphics annotation that emulates a rubber stamp effect.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var isActivatableTextField: Bool](pdfannotation/isactivatabletextfield.md)
- [var signatureAnnotationForRendering: Any?](pdfannotation/signatureannotationforrendering.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PDFAnnotationButtonWidget](pdfannotationbuttonwidget.md)
- [PDFAnnotationChoiceWidget](pdfannotationchoicewidget.md)
- [PDFAnnotationCircle](pdfannotationcircle.md)
- [PDFAnnotationFreeText](pdfannotationfreetext.md)
- [PDFAnnotationInk](pdfannotationink.md)
- [PDFAnnotationLine](pdfannotationline.md)
- [PDFAnnotationLink](pdfannotationlink.md)
- [PDFAnnotationMarkup](pdfannotationmarkup.md)
- [PDFAnnotationPopup](pdfannotationpopup.md)
- [PDFAnnotationSquare](pdfannotationsquare.md)
- [PDFAnnotationStamp](pdfannotationstamp.md)
- [PDFAnnotationText](pdfannotationtext.md)
- [PDFAnnotationTextWidget](pdfannotationtextwidget.md)
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

- [Adding Widgets to a PDF Document](adding-widgets-to-a-pdf-document.md)
  Add text, button, and choice widgets to a PDF document.
- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)
  Create and add custom annotation and page graphics to your PDF document.
- [Custom Graphics](custom-graphics.md)
  Demonstrates adding a watermark to a PDF page.
- [PDF Widgets](pdf-widgets.md)
  Demonstrates adding widgets—interactive form elements—to a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation)*