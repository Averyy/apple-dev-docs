# fieldName

**Framework**: PDFKit  
**Kind**: property

The widget identifier for form annotation actions and behaviors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var fieldName: String? { get set }
```

## Mentions

- [Adding Widgets to a PDF Document](adding-widgets-to-a-pdf-document.md)

#### Discussion

Use this identifier to refer to the widget when using a [`PDFActionResetForm`](pdfactionresetform.md) action.

## See Also

- [var widgetFieldType: PDFAnnotationWidgetSubtype](pdfannotation/widgetfieldtype.md)
  The type of widget annotation, such as button, choice, or text.
- [var widgetStringValue: String?](pdfannotation/widgetstringvalue.md)
  The string value of the widget annotation.
- [var widgetDefaultStringValue: String?](pdfannotation/widgetdefaultstringvalue.md)
  The string value that the widget reverts to when performing a reset form action.
- [var backgroundColor: UIColor?](pdfannotation/backgroundcolor.md)
  The color of the widget’s background.
- [var isReadOnly: Bool](pdfannotation/isreadonly.md)
  A Boolean value that determines whether the widget is editable.
- [enum PDFWidgetControlType](pdfwidgetcontroltype.md)
  The types of annotation buttons.
- [class PDFAppearanceCharacteristics](pdfappearancecharacteristics.md)
  An object that represents appearance characteristics of a widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/fieldname)*