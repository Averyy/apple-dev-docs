# bounds(for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounds of the selection on the specified page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func bounds(for page: PDFPage) -> CGRect
```

*macOS*

```swift
func bounds(for page: PDFPage) -> NSRect
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (CGRect) boundsForPage:(PDFPage *) page;
```

*macOS*

```objc
- (NSRect) boundsForPage:(PDFPage *) page;
```

## Discussion

The selection rectangle is given in page space.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Getting Information About a Selection
- [var pages: [PDFPage]](./pages.md)
  Returns the array of pages contained in the selection.
- [var string: String?](./string.md)
  Returns an `NSString` object representing the text contained in the selection (may contain linefeed characters).
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns an `NSAttributedString` object representing the text contained in the selection (may contain linefeed characters).
- [func selectionsByLine() -> [PDFSelection]](./selectionsbyline%28%29.md)
  Returns an array of selections, one for each line of text covered by the receiver.
- [var color: UIColor?](./color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/bounds(for:))*