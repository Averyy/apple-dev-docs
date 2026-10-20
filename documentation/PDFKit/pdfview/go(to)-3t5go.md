# go(to:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Scrolls to the first character of the specified selection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func go(to selection: PDFSelection)
```

```objc
- (void) goToSelection:(PDFSelection *) selection;
```

#### Discussion

PDF Kit records the move in its page history.

## See Also

### Using Seek in a Document
- [func go(to: PDFPage)](./go%28to%29-6x8y2.md)
  Scrolls to the specified page.
- [func go(to: PDFDestination)](./go%28to%29-5lh5d.md)
  Navigates to the specified destination.
- [func go(to: CGRect, on: PDFPage)](./go%28to,on%29.md)
  Navigates to the specified rectangle on the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/go(to:)-3t5go)*