# setAlignment(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the text alignment for the annotation.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setAlignment(_ alignment: NSTextAlignment)
```

```objc
- (void) setAlignment:(NSTextAlignment) alignment;
```

## Parameters

- `alignment`: The text-alignment value to be used for the annotation. Possible values are `NSLeftTextAlignment`, `NSRightTextAlignment`, and `NSCenterTextAlignment`.

## See Also

### Managing Background Color, Alignment, and Rotation
- [func backgroundColor() -> NSColor!](./backgroundcolor%28%29.md)
  Returns the background color of the annotation text field.
- [func setBackgroundColor(NSColor!)](./setbackgroundcolor%28_%29.md)
  Sets the background color of the annotation text field.
- [func alignment() -> NSTextAlignment](./alignment%28%29.md)
  Returns the text alignment setting for the annotation.
- [func rotation() -> Int](./rotation%28%29.md)
  Returns the rotation angle of the annotation text field in degrees.
- [func setRotation(Int32)](./setrotation%28_%29.md)
  Sets the rotation angle of the annotation text field in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/setalignment(_:))*