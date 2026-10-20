# setAlignment(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the horizontal alignment of text within the bounds of the annotation.

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

- `alignment`: Send `NSLeftTextAlignment`, `NSRightTextAlignment`, or `NSCenterTextAlignment` to set the horizontal alignment of text within the bounds of the annotation.

## See Also

### Managing Text Alignment
- [func alignment() -> NSTextAlignment](./alignment%28%29.md)
  Returns the horizontal alignment of text within the bounds of the annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationfreetext/setalignment(_:))*