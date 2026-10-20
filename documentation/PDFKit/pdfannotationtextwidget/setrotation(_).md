# setRotation(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the rotation angle of the annotation text field in degrees.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setRotation(_ rotation: Int32)
```

```objc
- (void) setRotation:(int) rotation;
```

## Parameters

- `rotation`: The rotation angle to be applied to the annotation text field, in degrees. The rotation angle must be a positive or negative multiple of 90 (negative angles are converted to their positive equivalents; for example -90 is changed to 270).

## See Also

### Related Documentation
- [class PDFAnnotationTextWidget](../pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
### Managing Background Color, Alignment, and Rotation
- [func backgroundColor() -> NSColor!](./backgroundcolor%28%29.md)
  Returns the background color of the annotation text field.
- [func setBackgroundColor(NSColor!)](./setbackgroundcolor%28_%29.md)
  Sets the background color of the annotation text field.
- [func alignment() -> NSTextAlignment](./alignment%28%29.md)
  Returns the text alignment setting for the annotation.
- [func setAlignment(NSTextAlignment)](./setalignment%28_%29.md)
  Sets the text alignment for the annotation.
- [func rotation() -> Int](./rotation%28%29.md)
  Returns the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/setrotation(_:))*