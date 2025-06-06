# PDFAppearanceCharacteristics

**Framework**: PDFKit  
**Kind**: class

An object that represents appearance characteristics of a widget annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFAppearanceCharacteristics
```

## Topics

### Configuring a Widget’s Appearance
- [var backgroundColor: UIColor?](pdfappearancecharacteristics/backgroundcolor.md)
  The background color of the widget annotation.
- [var borderColor: UIColor?](pdfappearancecharacteristics/bordercolor.md)
  The border color of the widget annotation.
- [var caption: String?](pdfappearancecharacteristics/caption.md)
  The text that the button widget annotation displays when the user isn’t interacting with it.
- [var controlType: PDFWidgetControlType](pdfappearancecharacteristics/controltype.md)
  The type of button widget annotation.
- [var downCaption: String?](pdfappearancecharacteristics/downcaption.md)
  The text that the button widget annotation displays when the user holds down on it.
- [var rolloverCaption: String?](pdfappearancecharacteristics/rollovercaption.md)
  The text that the widget annotation displays when the user hovers the pointer over it.
- [var rotation: Int](pdfappearancecharacteristics/rotation.md)
  The number of degrees, in multiples of 90, that the widget annotation rotates counterclockwise relative to the page.
- [var appearanceCharacteristicsKeyValues: [AnyHashable : Any]](pdfappearancecharacteristics/appearancecharacteristicskeyvalues.md)
  A dictionary that contains a deep copy of the appearance characteristic key-value pairs.
- [struct PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey.md)
  Keys to control a widget’s appearance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [enum PDFWidgetControlType](pdfwidgetcontroltype.md)
  The types of annotation buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfappearancecharacteristics)*