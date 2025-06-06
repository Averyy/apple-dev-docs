# index(for:)

**Framework**: PDFKit  
**Kind**: method

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

#### Discussion

Indexes are zero-based. This method raises an exception and returns `NSNotFound` if `page` is not found.

## See Also

- [var pageCount: Int](pdfdocument/pagecount.md)
  The number of pages in the document.
- [func page(at: Int) -> PDFPage?](pdfdocument/page(at:).md)
  Returns the page at the specified index number.
- [func insert(PDFPage, at: Int)](pdfdocument/insert(_:at:).md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](pdfdocument/removepage(at:).md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](pdfdocument/exchangepage(at:withpageat:).md)
  Swaps one page with another.
- [var pageClass: AnyClass](pdfdocument/pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/index(for:))*