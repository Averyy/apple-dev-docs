# allowsMultipleSelection

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether users can select multiple thumbnails in the thumbnail view at one time.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsMultipleSelection;
```

#### Return Value

[`true`](../../Swift/true.md) if users can select multiple thumbnails simultaneously, [`false`](../../Swift/false.md) otherwise.

#### Discussion

By default, `PDFThumbnailView` allows only a single thumbnail to be selected at one time. When this is the case, you can get the PDF page that corresponds to the selected thumbnail using the `PDFView` method [`currentPage`](../pdfview/currentpage.md).

When multiple selections are enabled, however, you must use [`selectedPages`](./selectedpages.md) to get the pages that correspond to the set of selected thumbnails.

## See Also

### Managing the Behavior of a Thumbnail View
- [var allowsDragging: Bool](./allowsdragging.md)
  Returns a Boolean value indicating whether users can drag thumbnails (that is, re-order pages in the document) within the thumbnail view.
- [var selectedPages: [PDFPage]?](./selectedpages.md)
  Returns an array of PDF pages that correspond to the selected thumbnails in the thumbnail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/allowsmultipleselection)*