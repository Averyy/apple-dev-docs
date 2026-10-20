# maximumNumberOfColumns

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the maximum number of columns of thumbnails the thumbnail view can display.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var maximumNumberOfColumns: Int { get set }
```

```objc
@property (nonatomic) NSUInteger maximumNumberOfColumns;
```

#### Return Value

The maximum number of columns of thumbnails the thumbnail view can display. If `0`, the thumbnail displays as many columns of thumbnails as fit in its size.

## See Also

### Working with Thumbnail View Display Characteristics
- [var labelFont: NSFont?](./labelfont.md)
  Returns the font used to label the thumbnails.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  Returns the color used in the background of the thumbnail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/maximumnumberofcolumns)*