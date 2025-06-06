# rotation()

**Framework**: PDFKit  
**Kind**: method

Returns the rotation angle of the annotation text field in degrees.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func rotation() -> Int
```

#### Return Value

The rotation angle of the annotation text field in degrees.

#### Discussion

Note that the rotation value is a positive multiple of 90, such as 0, 90, 180, or 270. The rotation of annotation text fields with negative rotation is converted to a corresponding positive rotation. For example, -90 is changed to 270.

## See Also

- [class PDFAnnotationTextWidget](pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
- [func backgroundColor() -> NSColor!](pdfannotationtextwidget/backgroundcolor.md)
  Returns the background color of the annotation text field.
- [func setBackgroundColor(NSColor!)](pdfannotationtextwidget/setbackgroundcolor(_:).md)
  Sets the background color of the annotation text field.
- [func alignment() -> NSTextAlignment](pdfannotationtextwidget/alignment.md)
  Returns the text alignment setting for the annotation.
- [func setAlignment(NSTextAlignment)](pdfannotationtextwidget/setalignment(_:).md)
  Sets the text alignment for the annotation.
- [func setRotation(Int32)](pdfannotationtextwidget/setrotation(_:).md)
  Sets the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/rotation())*