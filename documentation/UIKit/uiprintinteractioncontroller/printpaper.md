# printPaper

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that represents the paper size and printing area for the print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printPaper: UIPrintPaper? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIPrintPaper * printPaper;
```

#### Discussion

`UIPrintInteractionController` sets this property immediately after the user selects a printer and before it calls the delegate’s [`printInteractionControllerWillStartJob(_:)`](../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob%28_%29.md) method. If its delegate implements the [`printInteractionController(_:choosePaper:)`](../uiprintinteractioncontrollerdelegate/printinteractioncontroller%28_,choosepaper%29.md) method of the `UIPrintInteractionControllerDelegate` protocol, it can return the [`UIPrintPaper`](../uiprintpaper.md) object to assign to this property. Otherwise, UIKit assigns an object with a default paper size and printing rectangle that is based on the output type and the capabilities of the destination printer. This object is released when the print job finishes.

## See Also

### Accessing print-job information
- [var printInfo: UIPrintInfo?](./printinfo.md)
  An object that encapsulates information about the print job.
- [var showsNumberOfCopies: Bool](./showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperSelectionForLoadedPapers: Bool](./showspaperselectionforloadedpapers.md)
  A Boolean value that determines whether the paper selection menu displays.
- [var showsPaperOrientation: Bool](./showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.
- [var showsPageRange: Bool](./showspagerange.md)
  A Boolean value that determines whether the printing options include a page-range control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printpaper)*