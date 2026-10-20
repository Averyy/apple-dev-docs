# go(to:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Navigates to the specified destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func go(to destination: PDFDestination)
```

```objc
- (void) goToDestination:(PDFDestination *) destination;
```

#### Discussion

Destinations include a page and a point on the page specified in page space.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Related Documentation
- [var currentPage: PDFPage?](./currentpage.md)
  Returns the current page.
- [var currentDestination: PDFDestination?](./currentdestination.md)
  Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.
### Using Seek in a Document
- [func go(to: PDFPage)](./go%28to%29-6x8y2.md)
  Scrolls to the specified page.
- [func go(to: PDFSelection)](./go%28to%29-3t5go.md)
  Scrolls to the first character of the specified selection.
- [func go(to: CGRect, on: PDFPage)](./go%28to,on%29.md)
  Navigates to the specified rectangle on the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/go(to:)-5lh5d)*