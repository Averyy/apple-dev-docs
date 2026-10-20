# setBackgroundColor(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the background color of the annotation text field.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setBackgroundColor(_ color: NSColor!)
```

```objc
- (void) setBackgroundColor:(NSColor *) color;
```

## Parameters

- `color`: The color to be used in the background of the annotation’s text field.

## See Also

### Related Documentation
- [class PDFAnnotationTextWidget](../pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
### Managing Background Color, Alignment, and Rotation
- [func backgroundColor() -> NSColor!](./backgroundcolor%28%29.md)
  Returns the background color of the annotation text field.
- [func alignment() -> NSTextAlignment](./alignment%28%29.md)
  Returns the text alignment setting for the annotation.
- [func setAlignment(NSTextAlignment)](./setalignment%28_%29.md)
  Sets the text alignment for the annotation.
- [func rotation() -> Int](./rotation%28%29.md)
  Returns the rotation angle of the annotation text field in degrees.
- [func setRotation(Int32)](./setrotation%28_%29.md)
  Sets the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/setbackgroundcolor(_:))*