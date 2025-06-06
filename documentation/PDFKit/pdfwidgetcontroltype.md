# PDFWidgetControlType

**Framework**: PDFKit  
**Kind**: enum

The types of annotation buttons.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum PDFWidgetControlType
```

## Topics

### Constants
- [PDFWidgetControlType.unknownControl](pdfwidgetcontroltype/unknowncontrol.md)
  Unknown control type.
- [PDFWidgetControlType.pushButtonControl](pdfwidgetcontroltype/pushbuttoncontrol.md)
  Push button control.
- [PDFWidgetControlType.radioButtonControl](pdfwidgetcontroltype/radiobuttoncontrol.md)
  Radio button control.
- [PDFWidgetControlType.checkBoxControl](pdfwidgetcontroltype/checkboxcontrol.md)
  Check box control.
### Initializers
- [init?(rawValue: Int)](pdfwidgetcontroltype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [class PDFAppearanceCharacteristics](pdfappearancecharacteristics.md)
  An object that represents appearance characteristics of a widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfwidgetcontroltype)*