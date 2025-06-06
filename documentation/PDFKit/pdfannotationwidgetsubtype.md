# PDFAnnotationWidgetSubtype

**Framework**: PDFKit  
**Kind**: struct

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct PDFAnnotationWidgetSubtype
```

## Mentions

- [Adding Widgets to a PDF Document](adding-widgets-to-a-pdf-document.md)

## Topics

### Configuring a Widget Subtype
- [static let button: PDFAnnotationWidgetSubtype](pdfannotationwidgetsubtype/button.md)
  A button widget type, including push buttons, checkboxes, and radio buttons.
- [static let choice: PDFAnnotationWidgetSubtype](pdfannotationwidgetsubtype/choice.md)
  A type that presents a list of choices the user can choose from.
- [static let signature: PDFAnnotationWidgetSubtype](pdfannotationwidgetsubtype/signature.md)
  A digital signature widget type.
- [static let text: PDFAnnotationWidgetSubtype](pdfannotationwidgetsubtype/text.md)
  A text field the user can type text in.
### Creating a Widget Subtype
- [init(rawValue: String)](pdfannotationwidgetsubtype/init(rawvalue:).md)
  Creates a widget subtype using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let widgetAppearanceDictionary: PDFAnnotationKey](pdfannotationkey/widgetappearancedictionary.md)
  A dictionary or appearance characteristic object that contains properties for controlling the widget’s visual appearance.
- [static let widgetBackgroundColor: PDFAnnotationKey](pdfannotationkey/widgetbackgroundcolor.md)
  An array of floating point values or a PDF color object that specifies the widget’s background color.
- [static let widgetBorderColor: PDFAnnotationKey](pdfannotationkey/widgetbordercolor.md)
  An array of floating point values or a PDF color object that specifies the widget’s border color.
- [static let widgetCaption: PDFAnnotationKey](pdfannotationkey/widgetcaption.md)
  A string that a push button widget displays when it isn’t in a pressed state.
- [static let widgetDefaultValue: PDFAnnotationKey](pdfannotationkey/widgetdefaultvalue.md)
  A default value for the widget.
- [static let widgetDownCaption: PDFAnnotationKey](pdfannotationkey/widgetdowncaption.md)
  A string that a push button widgets displays when it’s in a pressed state.
- [static let widgetFieldFlags: PDFAnnotationKey](pdfannotationkey/widgetfieldflags.md)
  An integer value that specifies flags for a widget.
- [static let widgetFieldType: PDFAnnotationKey](pdfannotationkey/widgetfieldtype.md)
  A string that specifies the type of widget, such as button, checkbox, or signature field.
- [static let widgetMaxLen: PDFAnnotationKey](pdfannotationkey/widgetmaxlen.md)
  An integer value that specifies the maximum length of a text field, in characters.
- [static let widgetOptions: PDFAnnotationKey](pdfannotationkey/widgetoptions.md)
  An array that specifies the options to present in radio buttons or choice lists.
- [static let widgetRolloverCaption: PDFAnnotationKey](pdfannotationkey/widgetrollovercaption.md)
  A string that push button widgets display when the pointer is over the button, but not clicking it.
- [static let widgetRotation: PDFAnnotationKey](pdfannotationkey/widgetrotation.md)
  An integer value that specifies the rotation of the widget.
- [static let widgetTextLabelUI: PDFAnnotationKey](pdfannotationkey/widgettextlabelui.md)
  A user-visible alternative field name that identifies the widget, typically for accessibility purposes.
- [static let widgetValue: PDFAnnotationKey](pdfannotationkey/widgetvalue.md)
  The widget’s value, typically for text and choice widgets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationwidgetsubtype)*