# alignment()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the text alignment setting for the annotation.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func alignment() -> NSTextAlignment
```

```objc
- (NSTextAlignment) alignment;
```

#### Return Value

The text alignment value for the annotation. Supported alignment values are `NSLeftTextAlignment`, `NSRightTextAlignment`, and `NSCenterTextAlignment`.

## See Also

### Managing Background Color, Alignment, and Rotation
- [func backgroundColor() -> NSColor!](./backgroundcolor%28%29.md)
  Returns the background color of the annotation text field.
- [func setBackgroundColor(NSColor!)](./setbackgroundcolor%28_%29.md)
  Sets the background color of the annotation text field.
- [func setAlignment(NSTextAlignment)](./setalignment%28_%29.md)
  Sets the text alignment for the annotation.
- [func rotation() -> Int](./rotation%28%29.md)
  Returns the rotation angle of the annotation text field in degrees.
- [func setRotation(Int32)](./setrotation%28_%29.md)
  Sets the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/alignment())*