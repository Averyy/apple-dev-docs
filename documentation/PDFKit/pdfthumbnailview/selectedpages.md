# selectedPages

**Framework**: PDFKit  
**Kind**: property

Returns an array of PDF pages that correspond to the selected thumbnails in the thumbnail view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedPages: [PDFPage]? { get }
```

#### Return Value

An array of PDF pages that correspond to the thumbnails selected in the thumbnail view.

#### Discussion

If the thumbnail view allows multiple selections (if [`allowsMultipleSelection`](pdfthumbnailview/allowsmultipleselection.md) returns [`true`](https://developer.apple.com/documentation/swift/true)), you can use this method to get the PDF pages that correspond to the selected thumbnails.

## See Also

- [var allowsDragging: Bool](pdfthumbnailview/allowsdragging.md)
  Returns a Boolean value indicating whether users can drag thumbnails (that is, re-order pages in the document) within the thumbnail view.
- [var allowsMultipleSelection: Bool](pdfthumbnailview/allowsmultipleselection.md)
  Returns a Boolean value indicating whether users can select multiple thumbnails in the thumbnail view at one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/selectedpages)*