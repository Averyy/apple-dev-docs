# setEnd(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the ending point for the line.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setEnd(_ point: NSPoint)
```

```objc
- (void) setEndPoint:(NSPoint) point;
```

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `point`: The ending point for the line, in page space.

## See Also

### Specifying the Starting and Ending Points
- [func startPoint() -> NSPoint](./startpoint%28%29.md)
  Returns the starting point for the line.
- [func setStart(NSPoint)](./setstart%28_%29-86is0.md)
  Sets the starting point for the line.
- [func endPoint() -> NSPoint](./endpoint%28%29.md)
  Returns the ending point for the line in page space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/setend(_:)-2qn58)*