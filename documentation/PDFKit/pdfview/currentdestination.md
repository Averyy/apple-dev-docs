# currentDestination

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var currentDestination: PDFDestination? { get }
```

```objc
@property (nonatomic, readonly, nullable) PDFDestination * currentDestination;
```

#### Discussion

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Related Documentation
- [func go(to: PDFDestination)](./go%28to%29-5lh5d.md)
  Navigates to the specified destination.
### Navigating Within a Document
- [var currentPage: PDFPage?](./currentpage.md)
  Returns the current page.
- [var visiblePages: [PDFPage]](./visiblepages.md)
  Returns an array of `PDFPage` objects that represent the currently visible pages.
- [Navigation](../navigation.md)
  Operations for moving through page history and seeking to a page in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/currentdestination)*