# NSPrintInfo.PaginationMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the different ways in which an image is divided into pages.

**Availability**:
- macOS

## Declaration

```swift
enum PaginationMode
```

```c
enum NSPrintingPaginationMode : NSUInteger;
```

## Overview

These constants are used by [`horizontalPagination`](./horizontalpagination.md) and [`verticalPagination`](./verticalpagination.md).

## Topics

### Constants
- [NSPrintInfo.PaginationMode.automatic](./paginationmode/automatic.md)
- [NSPrintInfo.PaginationMode.fit](./paginationmode/fit.md)
- [NSPrintInfo.PaginationMode.clip](./paginationmode/clip.md)
### Initializers
- [init?(rawValue: UInt)](./paginationmode/init%28rawvalue%29.md)
### Deprecated
- [NSAutoPagination](../nsautopagination.md)
  The image is divided into equal-sized rectangles and placed in one column of pages.
- [NSFitPagination](../nsfitpagination.md)
  The image is scaled to produce one column or one row of pages.
- [NSClipPagination](../nsclippagination.md)
  The image is clipped to produce one column or row of pages.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Pagination
- [var horizontalPagination: NSPrintInfo.PaginationMode](./horizontalpagination.md)
  The horizontal pagination mode.
- [var verticalPagination: NSPrintInfo.PaginationMode](./verticalpagination.md)
  The vertical pagination to the specified mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/paginationmode)*