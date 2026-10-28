# NSPrintOperation.PageOrder

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the page order.

**Availability**:
- macOS

## Declaration

```swift
enum PageOrder
```

```c
enum NSPrintingPageOrder : NSInteger;
```

## Overview

These constants are used by [`pageOrder`](./pageorder-swift.property.md) and [`pageOrder`](./pageorder-swift.property.md).

## Topics

### Constants
- [NSPrintOperation.PageOrder.ascendingPageOrder](./pageorder-swift.enum/ascendingpageorder.md)
  Ascending (back to front) page order.
- [NSPrintOperation.PageOrder.descendingPageOrder](./pageorder-swift.enum/descendingpageorder.md)
  Descending (front to back) page order.
- [NSPrintOperation.PageOrder.specialPageOrder](./pageorder-swift.enum/specialpageorder.md)
  The spooler does not rearrange pages—they are printed in the order received by the spooler.
- [NSPrintOperation.PageOrder.unknownPageOrder](./pageorder-swift.enum/unknownpageorder.md)
  No page order specified.
### Initializers
- [init?(rawValue: Int)](./pageorder-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Page Information
- [var currentPage: Int](./currentpage.md)
  The current page number being printed.
- [var pageRange: NSRange](./pagerange.md)
  The range of pages associated with the print operation.
- [var pageOrder: NSPrintOperation.PageOrder](./pageorder-swift.property.md)
  The print order for the pages of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/pageorder-swift.enum)*