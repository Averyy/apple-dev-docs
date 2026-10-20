# setInteriorColor(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the color used to fill the ornament at the ends of the line.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setInteriorColor(_ color: NSColor!)
```

```objc
- (void) setInteriorColor:(NSColor *) color;
```

#### Discussion

The ornament at the end of a line is optional (for more information, see the Adobe PDF Specification 1.4).

## Parameters

- `color`: The color to be used to fill in the ornament at the ends of the line.

## See Also

### Specifying the Color of Line-end Ornaments
- [func interiorColor() -> NSColor!](./interiorcolor%28%29.md)
  Returns the color used to fill the ornament at the ends of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/setinteriorcolor(_:))*