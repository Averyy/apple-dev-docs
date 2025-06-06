# color

**Framework**: PDFKit  
**Kind**: property

Sets the color used for the drawing of a selection in both active and inactive states.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var color: UIColor? { get set }
```

#### Discussion

When no color has been specified for the `PDFSelection` objects in a document, the selections are drawn using `[NSColor selectedTextBackgroundColor]` for the active state and `[NSColor secondarySelectedControlColor]` for the inactive state. Use the `setColor` method to supply a color you want to be used for the drawing of both active and inactive selections.

## See Also

- [class PDFSelection](pdfselection.md)
  A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.
- [var pages: [PDFPage]](pdfselection/pages.md)
  Returns the array of pages contained in the selection.
- [var string: String?](pdfselection/string.md)
  Returns an `NSString` object representing the text contained in the selection (may contain linefeed characters).
- [var attributedString: NSAttributedString?](pdfselection/attributedstring.md)
  Returns an `NSAttributedString` object representing the text contained in the selection (may contain linefeed characters).
- [func bounds(for: PDFPage) -> CGRect](pdfselection/bounds(for:).md)
  Returns the bounds of the selection on the specified page.
- [func selectionsByLine() -> [PDFSelection]](pdfselection/selectionsbyline.md)
  Returns an array of selections, one for each line of text covered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/color)*