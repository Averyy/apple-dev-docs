# widgetValue

**Framework**: PDFKit  
**Kind**: property

The widget’s value, typically for text and choice widgets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let widgetValue: PDFAnnotationKey
```

#### Discussion

For radio button or checkbox widgets, the value for this key is typically `Off` if the button isn’t in a selected state; otherwise, [`buttonWidgetStateString`](pdfannotation/buttonwidgetstatestring.md).

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
- [struct PDFAnnotationWidgetSubtype](pdfannotationwidgetsubtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey/widgetvalue)*