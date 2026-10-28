# index(for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Gets the index number for the specified page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func index(for page: PDFPage) -> Int
```

```objc
- (NSUInteger) indexForPage:(PDFPage *) page;
```

## Discussion

Indexes are zero-based. This method raises an exception and returns `NSNotFound` if `page` is not found.

## See Also

### Working with Pages
- [var pageCount: Int](./pagecount.md)
  The number of pages in the document.
- [func page(at: Int) -> PDFPage?](./page%28at%29.md)
  Returns the page at the specified index number.
- [func insert(PDFPage, at: Int)](./insert%28_,at%29.md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](./removepage%28at%29.md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](./exchangepage%28at,withpageat%29.md)
  Swaps one page with another.
- [var pageClass: AnyClass](./pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/index(for:))*