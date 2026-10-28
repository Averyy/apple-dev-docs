# insert(_:at:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Inserts a page at the specified index point.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func insert(_ page: PDFPage, at index: Int)
```

```objc
- (void) insertPage:(PDFPage *) page atIndex:(NSUInteger) index;
```

## Discussion

This method raises an exception if `index` is out of bounds.

Be aware that a PDF viewing application might use the size of the first page in the document as representative of all page sizes when reporting the size of a document. If you need to get the actual size of an individual page, you can use [`bounds(for:)`](../pdfpage/bounds%28for%29.md) (note that the size is returned in points, which are typically converted to inches or centimeters by PDF viewing applications).

## See Also

### Working with Pages
- [var pageCount: Int](./pagecount.md)
  The number of pages in the document.
- [func page(at: Int) -> PDFPage?](./page%28at%29.md)
  Returns the page at the specified index number.
- [func index(for: PDFPage) -> Int](./index%28for%29.md)
  Gets the index number for the specified page.
- [func removePage(at: Int)](./removepage%28at%29.md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](./exchangepage%28at,withpageat%29.md)
  Swaps one page with another.
- [var pageClass: AnyClass](./pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/insert(_:at:))*