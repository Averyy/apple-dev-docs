# PDFAppearanceCharacteristicsKey

**Framework**: PDFKit  
**Kind**: struct

Keys to control a widget’s appearance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct PDFAppearanceCharacteristicsKey
```

## Topics

### Modifying Widget Appearance
- [static let backgroundColor: PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey/backgroundcolor.md)
  The background color of the widget annotation.
- [static let borderColor: PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey/bordercolor.md)
  The border color of the widget annotation.
- [static let caption: PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey/caption.md)
  The text that the button widget annotation displays when the user isn’t interacting with it.
- [static let downCaption: PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey/downcaption.md)
  The text that the button widget annotation displays when the user holds down on it.
- [static let rolloverCaption: PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey/rollovercaption.md)
  The text that the button widget annotation displays when the user hovers the pointer over it.
- [static let rotation: PDFAppearanceCharacteristicsKey](pdfappearancecharacteristicskey/rotation.md)
  The number of degrees, in multiples of 90, that the widget annotation rotates counterclockwise relative to the page.
### Creating an Appearance Characteristic Key
- [init(rawValue: String)](pdfappearancecharacteristicskey/init(rawvalue:).md)
  Creates an appearance characteristic key using the specified raw string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfappearancecharacteristicskey)*