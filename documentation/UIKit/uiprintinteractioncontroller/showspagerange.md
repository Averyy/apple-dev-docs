# showsPageRange

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the printing options include a page-range control.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsPageRange: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). If you assign printable content to the [`printingItems`](uiprintinteractioncontroller/printingitems.md) property, the page-range control is not shown, even if `showPageRange` is [`true`](https://developer.apple.com/documentation/swift/true). In other cases, the number of pages to print must be greater than 1 form the page-range control to appear.

## See Also

- [var printInfo: UIPrintInfo?](uiprintinteractioncontroller/printinfo.md)
  An object that encapsulates information about the print job.
- [var printPaper: UIPrintPaper?](uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var showsNumberOfCopies: Bool](uiprintinteractioncontroller/showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperSelectionForLoadedPapers: Bool](uiprintinteractioncontroller/showspaperselectionforloadedpapers.md)
  A Boolean value that determines whether the paper selection menu displays.
- [var showsPaperOrientation: Bool](uiprintinteractioncontroller/showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspagerange)*