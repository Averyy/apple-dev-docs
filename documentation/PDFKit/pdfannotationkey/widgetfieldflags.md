# widgetFieldFlags

**Framework**: PDFKit  
**Kind**: property  
**Role**: Type Property

An integer value that specifies flags for a widget.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let widgetFieldFlags: PDFAnnotationKey
```

```c
extern PDFAnnotationKey PDFAnnotationKeyWidgetFieldFlags;
```

#### Discussion

For a full description of the possible widget field flags, see [Table 221](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf#page=441), [Table 226](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf#page=447), [Table 228](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf#page=451), and [Table 230](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf#page=452) in the [Adobe PDF 1.7 Specification](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf).

## See Also

### Configuring Widget Annotations
- [static let widgetAppearanceDictionary: PDFAnnotationKey](./widgetappearancedictionary.md)
  A dictionary or appearance characteristic object that contains properties for controlling the widget’s visual appearance.
- [static let widgetBackgroundColor: PDFAnnotationKey](./widgetbackgroundcolor.md)
  An array of floating point values or a PDF color object that specifies the widget’s background color.
- [static let widgetBorderColor: PDFAnnotationKey](./widgetbordercolor.md)
  An array of floating point values or a PDF color object that specifies the widget’s border color.
- [static let widgetCaption: PDFAnnotationKey](./widgetcaption.md)
  A string that a push button widget displays when it isn’t in a pressed state.
- [static let widgetDefaultValue: PDFAnnotationKey](./widgetdefaultvalue.md)
  A default value for the widget.
- [static let widgetDownCaption: PDFAnnotationKey](./widgetdowncaption.md)
  A string that a push button widgets displays when it’s in a pressed state.
- [static let widgetFieldType: PDFAnnotationKey](./widgetfieldtype.md)
  A string that specifies the type of widget, such as button, checkbox, or signature field.
- [static let widgetMaxLen: PDFAnnotationKey](./widgetmaxlen.md)
  An integer value that specifies the maximum length of a text field, in characters.
- [static let widgetOptions: PDFAnnotationKey](./widgetoptions.md)
  An array that specifies the options to present in radio buttons or choice lists.
- [static let widgetRolloverCaption: PDFAnnotationKey](./widgetrollovercaption.md)
  A string that push button widgets display when the pointer is over the button, but not clicking it.
- [static let widgetRotation: PDFAnnotationKey](./widgetrotation.md)
  An integer value that specifies the rotation of the widget.
- [static let widgetTextLabelUI: PDFAnnotationKey](./widgettextlabelui.md)
  A user-visible alternative field name that identifies the widget, typically for accessibility purposes.
- [static let widgetValue: PDFAnnotationKey](./widgetvalue.md)
  The widget’s value, typically for text and choice widgets.
- [struct PDFAnnotationWidgetSubtype](../pdfannotationwidgetsubtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey/widgetfieldflags)*