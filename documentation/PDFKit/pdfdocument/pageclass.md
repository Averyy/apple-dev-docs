# pageClass

**Framework**: PDFKit  
**Kind**: property

The class that is allocated and initialized when page objects are created for the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var pageClass: AnyClass { get }
```

#### Discussion

If you want to supply a custom page class, subclass `PDFDocument` and implement this method to return your custom class. Note that your custom class must be a subclass of [`PDFPage`](pdfpage.md); otherwise, the behavior is undefined.

The default implementation of `pageClass` returns `[PDFPage class]`.

## See Also

- [var pageCount: Int](pdfdocument/pagecount.md)
  The number of pages in the document.
- [func page(at: Int) -> PDFPage?](pdfdocument/page(at:).md)
  Returns the page at the specified index number.
- [func index(for: PDFPage) -> Int](pdfdocument/index(for:).md)
  Gets the index number for the specified page.
- [func insert(PDFPage, at: Int)](pdfdocument/insert(_:at:).md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](pdfdocument/removepage(at:).md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](pdfdocument/exchangepage(at:withpageat:).md)
  Swaps one page with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/pageclass)*