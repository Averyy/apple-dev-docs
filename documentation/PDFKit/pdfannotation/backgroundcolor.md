# backgroundColor

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The color of the widget’s background.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
@NSCopying
var backgroundColor: UIColor? { get set }
```

*macOS*

```swift
@NSCopying
var backgroundColor: NSColor? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) UIColor * backgroundColor;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSColor * backgroundColor;
```

## See Also

### Configuring Widget Annotations
- [var widgetFieldType: PDFAnnotationWidgetSubtype](./widgetfieldtype.md)
  The type of widget annotation, such as button, choice, or text.
- [var widgetStringValue: String?](./widgetstringvalue.md)
  The string value of the widget annotation.
- [var widgetDefaultStringValue: String?](./widgetdefaultstringvalue.md)
  The string value that the widget reverts to when performing a reset form action.
- [var fieldName: String?](./fieldname.md)
  The widget identifier for form annotation actions and behaviors.
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that determines whether the widget is editable.
- [enum PDFWidgetControlType](../pdfwidgetcontroltype.md)
  The types of annotation buttons.
- [class PDFAppearanceCharacteristics](../pdfappearancecharacteristics.md)
  An object that represents appearance characteristics of a widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/backgroundcolor)*