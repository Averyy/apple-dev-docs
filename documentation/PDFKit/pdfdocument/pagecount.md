# pageCount

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The number of pages in the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var pageCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger pageCount;
```

## See Also

### Working with Pages
- [func page(at: Int) -> PDFPage?](./page%28at%29.md)
  Returns the page at the specified index number.
- [func index(for: PDFPage) -> Int](./index%28for%29.md)
  Gets the index number for the specified page.
- [func insert(PDFPage, at: Int)](./insert%28_,at%29.md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](./removepage%28at%29.md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](./exchangepage%28at,withpageat%29.md)
  Swaps one page with another.
- [var pageClass: AnyClass](./pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/pagecount)*