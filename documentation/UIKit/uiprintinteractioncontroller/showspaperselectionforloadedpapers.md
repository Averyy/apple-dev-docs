# showsPaperSelectionForLoadedPapers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the paper selection menu displays.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var showsPaperSelectionForLoadedPapers: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsPaperSelectionForLoadedPapers;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). Setting the value to [`true`](../../Swift/true.md) enables a paper selection menu on printers that support different types of paper and have more than one paper type loaded. On printers where only one paper type is available, no paper selection menu is displayed, regardless of the value of this property.

## See Also

### Accessing print-job information
- [var printInfo: UIPrintInfo?](./printinfo.md)
  An object that encapsulates information about the print job.
- [var printPaper: UIPrintPaper?](./printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var showsNumberOfCopies: Bool](./showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperOrientation: Bool](./showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.
- [var showsPageRange: Bool](./showspagerange.md)
  A Boolean value that determines whether the printing options include a page-range control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspaperselectionforloadedpapers)*