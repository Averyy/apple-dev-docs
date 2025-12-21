# backgroundColor

**Framework**: PDFKit  
**Kind**: property

The view’s background color.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backgroundColor: NSColor { get set }
```

#### Discussion

A view’s background is the area displayed to either side of a PDF document’s pages. The background also appears between pages when page breaks are enabled. The default color is a 50% gray.

## See Also

- [func takeBackgroundColorFrom(Any)](pdfview/takebackgroundcolorfrom(_:).md)
  Sets the view’s background color to the specified color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/backgroundcolor)*