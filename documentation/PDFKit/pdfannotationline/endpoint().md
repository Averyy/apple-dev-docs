# endPoint()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the ending point for the line in page space.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func endPoint() -> NSPoint
```

```objc
- (NSPoint) endPoint;
```

#### Return Value

The ending point for the line, in page space.

#### Discussion

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Specifying the Starting and Ending Points
- [func startPoint() -> NSPoint](./startpoint%28%29.md)
  Returns the starting point for the line.
- [func setStart(NSPoint)](./setstart%28_%29-86is0.md)
  Sets the starting point for the line.
- [func setEnd(NSPoint)](./setend%28_%29-2qn58.md)
  Sets the ending point for the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationline/endpoint())*