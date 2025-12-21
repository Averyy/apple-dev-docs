# allowsDragging

**Framework**: PDFKit  
**Kind**: property

Returns a Boolean value indicating whether users can drag thumbnails (that is, re-order pages in the document) within the thumbnail view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var allowsDragging: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if users can re-order pages by dragging thumbnails, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [var allowsMultipleSelection: Bool](pdfthumbnailview/allowsmultipleselection.md)
  Returns a Boolean value indicating whether users can select multiple thumbnails in the thumbnail view at one time.
- [var selectedPages: [PDFPage]?](pdfthumbnailview/selectedpages.md)
  Returns an array of PDF pages that correspond to the selected thumbnails in the thumbnail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/allowsdragging)*