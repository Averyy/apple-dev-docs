# NSPrintOperation.PageOrder

**Framework**: AppKit  
**Kind**: enum

Constants that specify the page order.

**Availability**:
- macOS ?+

## Declaration

```swift
enum PageOrder
```

#### Overview

These constants are used by [`pageOrder`](nsprintoperation/pageorder-swift.property.md) and [`pageOrder`](nsprintoperation/pageorder-swift.property.md).

## Topics

### Constants
- [NSPrintOperation.PageOrder.ascendingPageOrder](nsprintoperation/pageorder-swift.enum/ascendingpageorder.md)
  Ascending (back to front) page order.
- [NSPrintOperation.PageOrder.descendingPageOrder](nsprintoperation/pageorder-swift.enum/descendingpageorder.md)
  Descending (front to back) page order.
- [NSPrintOperation.PageOrder.specialPageOrder](nsprintoperation/pageorder-swift.enum/specialpageorder.md)
  The spooler does not rearrange pages—they are printed in the order received by the spooler.
- [NSPrintOperation.PageOrder.unknownPageOrder](nsprintoperation/pageorder-swift.enum/unknownpageorder.md)
  No page order specified.
### Initializers
- [init?(rawValue: Int)](nsprintoperation/pageorder-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var currentPage: Int](nsprintoperation/currentpage.md)
  The current page number being printed.
- [var pageRange: NSRange](nsprintoperation/pagerange.md)
  The range of pages associated with the print operation.
- [var pageOrder: NSPrintOperation.PageOrder](nsprintoperation/pageorder-swift.property.md)
  The print order for the pages of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/pageorder-swift.enum)*