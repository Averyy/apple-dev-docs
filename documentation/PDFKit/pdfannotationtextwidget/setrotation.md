# setRotation(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the rotation angle of the annotation text field in degrees.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setRotation(_ rotation: Int32)
```

## Parameters

- `rotation`: The rotation angle to be applied to the annotation text field, in degrees. The rotation angle must be a positive or negative multiple of 90 (negative angles are converted to their positive equivalents; for example -90 is changed to 270).

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
- [func rotation() -> Int](pdfannotationtextwidget/rotation.md)
  Returns the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/setrotation(_:))*