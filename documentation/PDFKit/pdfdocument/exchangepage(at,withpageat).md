# exchangePage(at:withPageAt:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Swaps one page with another.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func exchangePage(at indexA: Int, withPageAt indexB: Int)
```

```objc
- (void) exchangePageAtIndex:(NSUInteger) indexA withPageAtIndex:(NSUInteger) indexB;
```

## Discussion

This method raises an exception if either `index` value is out of bounds.

## See Also

### Working with Pages
- [var pageCount: Int](./pagecount.md)
  The number of pages in the document.
- [func page(at: Int) -> PDFPage?](./page%28at%29.md)
  Returns the page at the specified index number.
- [func index(for: PDFPage) -> Int](./index%28for%29.md)
  Gets the index number for the specified page.
- [func insert(PDFPage, at: Int)](./insert%28_,at%29.md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](./removepage%28at%29.md)
  Removes the page at the specified index point.
- [var pageClass: AnyClass](./pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/exchangepage(at:withpageat:))*