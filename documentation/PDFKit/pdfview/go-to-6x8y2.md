# go(to:)

**Framework**: PDFKit  
**Kind**: method

Scrolls to the specified page.

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
func go(to page: PDFPage)
```

#### Discussion

PDF Kit records the move in its page history.

## See Also

- [func go(to: PDFDestination)](pdfview/go(to:)-5lh5d.md)
  Navigates to the specified destination.
- [func go(to: PDFSelection)](pdfview/go(to:)-3t5go.md)
  Scrolls to the first character of the specified selection.
- [func go(to: CGRect, on: PDFPage)](pdfview/go(to:on:).md)
  Navigates to the specified rectangle on the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/go(to:)-6x8y2)*