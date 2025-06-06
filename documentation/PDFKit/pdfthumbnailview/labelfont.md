# labelFont

**Framework**: PDFKit  
**Kind**: property

Returns the font used to label the thumbnails.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
@MainActor var labelFont: NSFont? { get set }
```

#### Return Value

The font used in the thumbnail labels.

#### Discussion

Typically, the label of a thumbnail is the page number of the page it represents.

## See Also

- [var maximumNumberOfColumns: Int](pdfthumbnailview/maximumnumberofcolumns.md)
  Returns the maximum number of columns of thumbnails the thumbnail view can display.
- [var backgroundColor: UIColor?](pdfthumbnailview/backgroundcolor.md)
  Returns the color used in the background of the thumbnail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/labelfont)*