# rotation()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the rotation angle of the annotation text field in degrees.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func rotation() -> Int
```

```objc
- (NSInteger) rotation;
```

## Return Value

The rotation angle of the annotation text field in degrees.

## Discussion

Note that the rotation value is a positive multiple of 90, such as 0, 90, 180, or 270. The rotation of annotation text fields with negative rotation is converted to a corresponding positive rotation. For example, -90 is changed to 270.

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
- [func setRotation(Int32)](./setrotation%28_%29.md)
  Sets the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/rotation())*