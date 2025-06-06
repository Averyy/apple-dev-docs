# setEnd(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the ending point for the line.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setEnd(_ point: NSPoint)
```

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `point`: The ending point for the line, in page space.

## See Also

- [func startPoint() -> NSPoint](pdfannotationline/startpoint.md)
  Returns the starting point for the line.
- [func setStart(NSPoint)](pdfannotationline/setstart(_:)-86is0.md)
  Sets the starting point for the line.
- [func endPoint() -> NSPoint](pdfannotationline/endpoint.md)
  Returns the ending point for the line in page space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/setend(_:)-2qn58)*