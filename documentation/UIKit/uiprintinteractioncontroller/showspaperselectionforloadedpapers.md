# showsPaperSelectionForLoadedPapers

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the paper selection menu displays.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsPaperSelectionForLoadedPapers: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). Setting the value to [`true`](https://developer.apple.com/documentation/Swift/true) enables a paper selection menu on printers that support different types of paper and have more than one paper type loaded. On printers where only one paper type is available, no paper selection menu is displayed, regardless of the value of this property.

## See Also

- [var printInfo: UIPrintInfo?](uiprintinteractioncontroller/printinfo.md)
  An object that encapsulates information about the print job.
- [var printPaper: UIPrintPaper?](uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var showsNumberOfCopies: Bool](uiprintinteractioncontroller/showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperOrientation: Bool](uiprintinteractioncontroller/showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.
- [var showsPageRange: Bool](uiprintinteractioncontroller/showspagerange.md)
  A Boolean value that determines whether the printing options include a page-range control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspaperselectionforloadedpapers)*