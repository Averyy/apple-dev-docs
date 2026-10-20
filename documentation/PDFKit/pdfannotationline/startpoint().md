# startPoint()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the starting point for the line.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func startPoint() -> NSPoint
```

```objc
- (NSPoint) startPoint;
```

#### Return Value

The starting point for the line, in page space.

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Specifying the Starting and Ending Points
- [func setStart(NSPoint)](./setstart%28_%29-86is0.md)
  Sets the starting point for the line.
- [func endPoint() -> NSPoint](./endpoint%28%29.md)
  Returns the ending point for the line in page space.
- [func setEnd(NSPoint)](./setend%28_%29-2qn58.md)
  Sets the ending point for the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/startpoint())*