# selection(from:to:)

**Framework**: PDFKit  
**Kind**: method

Returns the text between the two specified points in page space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func selection(from startPoint: CGPoint, to endPoint: CGPoint) -> PDFSelection?
```

#### Discussion

Either point may be the one closer to the start of the page. In determining the selection, the points are sorted first top to bottom and then left to right.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

To visualize the selection, picture the rectangle defined by `startPoint` and `endPoint`. The selection begins at the first character fully within the defined rectangle and closest to its upper-left corner. The selection ends at the last character fully within the defined rectangle and closest to its lower-right corner.

## See Also

- [func selection(for: CGRect) -> PDFSelection?](pdfpage/selection(for:)-2ckpi.md)
  Returns the text enclosed within the specified rectangle, expressed in page (user) coordinates.
- [func selectionForWord(at: CGPoint) -> PDFSelection?](pdfpage/selectionforword(at:).md)
  Returns the whole word that includes the specified point.
- [func selectionForLine(at: CGPoint) -> PDFSelection?](pdfpage/selectionforline(at:).md)
  Returns the whole line of text that includes the specified point.
- [func selection(for: NSRange) -> PDFSelection?](pdfpage/selection(for:)-20y9d.md)
  Returns the text contained within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/selection(from:to:))*