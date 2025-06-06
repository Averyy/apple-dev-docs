# page(at:)

**Framework**: PDFKit  
**Kind**: method

Returns the page at the specified index number.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func page(at index: Int) -> PDFPage?
```

#### Discussion

Indexes are zero based. This method raises an exception if `index` is out of bounds.

## See Also

- [var pageCount: Int](pdfdocument/pagecount.md)
  The number of pages in the document.
- [func index(for: PDFPage) -> Int](pdfdocument/index(for:).md)
  Gets the index number for the specified page.
- [func insert(PDFPage, at: Int)](pdfdocument/insert(_:at:).md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](pdfdocument/removepage(at:).md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](pdfdocument/exchangepage(at:withpageat:).md)
  Swaps one page with another.
- [var pageClass: AnyClass](pdfdocument/pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/page(at:))*