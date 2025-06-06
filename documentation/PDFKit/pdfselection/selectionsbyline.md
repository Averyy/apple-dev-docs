# selectionsByLine()

**Framework**: PDFKit  
**Kind**: method

Returns an array of selections, one for each line of text covered by the receiver.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func selectionsByLine() -> [PDFSelection]
```

#### Discussion

If you call this method on a `PDFSelection` object that represents a paragraph, for example, `selectionsByLine` returns an array that contains one `PDFSelection` object for each line of text in the paragraph.

## See Also

- [var pages: [PDFPage]](pdfselection/pages.md)
  Returns the array of pages contained in the selection.
- [var string: String?](pdfselection/string.md)
  Returns an `NSString` object representing the text contained in the selection (may contain linefeed characters).
- [var attributedString: NSAttributedString?](pdfselection/attributedstring.md)
  Returns an `NSAttributedString` object representing the text contained in the selection (may contain linefeed characters).
- [func bounds(for: PDFPage) -> CGRect](pdfselection/bounds(for:).md)
  Returns the bounds of the selection on the specified page.
- [var color: UIColor?](pdfselection/color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/selectionsbyline())*