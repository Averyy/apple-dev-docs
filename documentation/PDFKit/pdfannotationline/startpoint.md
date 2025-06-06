# startPoint()

**Framework**: PDFKit  
**Kind**: method

Returns the starting point for the line.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func startPoint() -> NSPoint
```

#### Return Value

The starting point for the line, in page space.

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [func setStart(NSPoint)](pdfannotationline/setstart(_:)-86is0.md)
  Sets the starting point for the line.
- [func endPoint() -> NSPoint](pdfannotationline/endpoint.md)
  Returns the ending point for the line in page space.
- [func setEnd(NSPoint)](pdfannotationline/setend(_:)-2qn58.md)
  Sets the ending point for the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/startpoint())*