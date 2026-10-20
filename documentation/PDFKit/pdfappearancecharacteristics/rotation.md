# rotation

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The number of degrees, in multiples of 90, that the widget annotation rotates counterclockwise relative to the page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var rotation: Int { get set }
```

```objc
@property (nonatomic) NSInteger rotation;
```

## See Also

### Configuring a Widget’s Appearance
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The background color of the widget annotation.
- [var borderColor: UIColor?](./bordercolor.md)
  The border color of the widget annotation.
- [var caption: String?](./caption.md)
  The text that the button widget annotation displays when the user isn’t interacting with it.
- [var controlType: PDFWidgetControlType](./controltype.md)
  The type of button widget annotation.
- [var downCaption: String?](./downcaption.md)
  The text that the button widget annotation displays when the user holds down on it.
- [var rolloverCaption: String?](./rollovercaption.md)
  The text that the widget annotation displays when the user hovers the pointer over it.
- [var appearanceCharacteristicsKeyValues: [AnyHashable : Any]](./appearancecharacteristicskeyvalues.md)
  A dictionary that contains a deep copy of the appearance characteristic key-value pairs.
- [struct PDFAppearanceCharacteristicsKey](../pdfappearancecharacteristicskey.md)
  Keys to control a widget’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfappearancecharacteristics/rotation)*