# selectionForLine(at:)

**Framework**: PDFKit  
**Kind**: method

Returns the whole line of text that includes the specified point.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func selectionForLine(at point: CGPoint) -> PDFSelection?
```

#### Discussion

Returns `NULL` if no line of text contains `point`.

Use this method to respond to a triple-click.

## See Also

- [func selection(for: CGRect) -> PDFSelection?](pdfpage/selection(for:)-2ckpi.md)
  Returns the text enclosed within the specified rectangle, expressed in page (user) coordinates.
- [func selectionForWord(at: CGPoint) -> PDFSelection?](pdfpage/selectionforword(at:).md)
  Returns the whole word that includes the specified point.
- [func selection(from: CGPoint, to: CGPoint) -> PDFSelection?](pdfpage/selection(from:to:).md)
  Returns the text between the two specified points in page space.
- [func selection(for: NSRange) -> PDFSelection?](pdfpage/selection(for:)-20y9d.md)
  Returns the text contained within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/selectionforline(at:))*