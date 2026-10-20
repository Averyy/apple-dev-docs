# draw(_:to:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Draw and render a visible page to a context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func draw(_ page: PDFPage, to context: CGContext)
```

```objc
- (void) drawPage:(PDFPage *) page toContext:(CGContextRef) context;
```

## See Also

### Drawing in a PDF Page
- [func drawPagePost(PDFPage, to: CGContext)](./drawpagepost%28_,to%29.md)
  Perform post-page rendering for a page rendered to a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/draw(_:to:))*