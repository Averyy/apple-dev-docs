# pageRange

**Framework**: AppKit  
**Kind**: property

The range of pages associated with the print operation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var pageRange: NSRange { get }
```

#### Return Value

The range of page numbers. Page numbers are one-based values where the index of page one is 1, the index of page two is 2, and so on. Depending on the information returned by the printing view, the starting page number may not be 1.  Also, if the number of pages being printed is not known, the page count may be set to `NSIntegerMax`.

## See Also

- [func knowsPageRange(NSRangePointer) -> Bool](nsview/knowspagerange(_:).md)
  Returns [`true`](https://developer.apple.com/documentation/swift/true) if the view handles page boundaries, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.
- [var currentPage: Int](nsprintoperation/currentpage.md)
  The current page number being printed.
- [var pageOrder: NSPrintOperation.PageOrder](nsprintoperation/pageorder-swift.property.md)
  The print order for the pages of the operation.
- [NSPrintOperation.PageOrder](nsprintoperation/pageorder-swift.enum.md)
  Constants that specify the page order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/pagerange)*