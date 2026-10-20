# showsPageRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the printing options include a page-range control.

**Availability**:
- iOS 4.2+ - Deprecated in 10.0
- iPadOS 4.2+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: The print interaction controller always shows the page range because a person can remove pages from the print preview.

## Declaration

```swift
var showsPageRange: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsPageRange;
```

#### Discussion

The default value is [`false`](../../Swift/false.md). If you assign printable content to the [`printingItems`](./printingitems.md) property, the page-range control is not shown, even if `showPageRange` is [`true`](../../Swift/true.md). In other cases, the number of pages to print must be greater than 1 form the page-range control to appear.

## See Also

### Accessing print-job information
- [var printInfo: UIPrintInfo?](./printinfo.md)
  An object that encapsulates information about the print job.
- [var printPaper: UIPrintPaper?](./printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var showsNumberOfCopies: Bool](./showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperSelectionForLoadedPapers: Bool](./showspaperselectionforloadedpapers.md)
  A Boolean value that determines whether the paper selection menu displays.
- [var showsPaperOrientation: Bool](./showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspagerange)*