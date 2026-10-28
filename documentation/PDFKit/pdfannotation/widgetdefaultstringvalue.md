# widgetDefaultStringValue

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The string value that the widget reverts to when performing a reset form action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var widgetDefaultStringValue: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * widgetDefaultStringValue;
```

## Discussion

For text and choice widgets, this property specifies the string value that a reset form action sets on a widget.

For radio buttons and checkboxes, set this property to `Off` if the desired default is for the button to be in an unselected state; otherwise, set it to the [`buttonWidgetStateString`](./buttonwidgetstatestring.md).

## See Also

### Configuring Widget Annotations
- [var widgetFieldType: PDFAnnotationWidgetSubtype](./widgetfieldtype.md)
  The type of widget annotation, such as button, choice, or text.
- [var widgetStringValue: String?](./widgetstringvalue.md)
  The string value of the widget annotation.
- [var fieldName: String?](./fieldname.md)
  The widget identifier for form annotation actions and behaviors.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color of the widget’s background.
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that determines whether the widget is editable.
- [enum PDFWidgetControlType](../pdfwidgetcontroltype.md)
  The types of annotation buttons.
- [class PDFAppearanceCharacteristics](../pdfappearancecharacteristics.md)
  An object that represents appearance characteristics of a widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/widgetdefaultstringvalue)*