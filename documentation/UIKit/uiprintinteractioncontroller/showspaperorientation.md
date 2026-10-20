# showsPaperOrientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the printing options include the paper-orientation control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var showsPaperOrientation: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsPaperOrientation;
```

#### Discussion

The default value is [`true`](../../Swift/true.md).

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
- [var showsPageRange: Bool](./showspagerange.md)
  A Boolean value that determines whether the printing options include a page-range control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/showspaperorientation)*