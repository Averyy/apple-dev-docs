# allowsDragging

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether users can drag thumbnails (that is, re-order pages in the document) within the thumbnail view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var allowsDragging: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsDragging;
```

#### Return Value

[`true`](../../Swift/true.md) if users can re-order pages by dragging thumbnails, [`false`](../../Swift/false.md) otherwise.

## See Also

### Managing the Behavior of a Thumbnail View
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  Returns a Boolean value indicating whether users can select multiple thumbnails in the thumbnail view at one time.
- [var selectedPages: [PDFPage]?](./selectedpages.md)
  Returns an array of PDF pages that correspond to the selected thumbnails in the thumbnail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/allowsdragging)*