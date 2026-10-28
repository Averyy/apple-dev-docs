# bounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image representation’s bounding rectangle.

**Availability**:
- macOS

## Declaration

```swift
var bounds: NSRect { get }
```

```objc
@property (readonly) NSRect bounds;
```

## Discussion

This value is equivalent to the crop box specified by the PDF data.

## See Also

### Getting Data
- [var currentPage: Int](./currentpage.md)
  The page currently displayed by the image representation.
- [var pageCount: Int](./pagecount.md)
  The number of pages in the image representation.
- [var pdfRepresentation: Data](./pdfrepresentation.md)
  The PDF representation of the representation’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfimagerep/bounds)*