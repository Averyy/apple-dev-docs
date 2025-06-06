# setStart(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the starting point for the line.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setStart(_ point: NSPoint)
```

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `point`: The starting point for the line, in page space.

## See Also

- [func startPoint() -> NSPoint](pdfannotationline/startpoint.md)
  Returns the starting point for the line.
- [func endPoint() -> NSPoint](pdfannotationline/endpoint.md)
  Returns the ending point for the line in page space.
- [func setEnd(NSPoint)](pdfannotationline/setend(_:)-2qn58.md)
  Sets the ending point for the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/setstart(_:)-86is0)*