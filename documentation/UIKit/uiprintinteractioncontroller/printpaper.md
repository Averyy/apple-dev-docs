# printPaper

**Framework**: UIKit  
**Kind**: property

An object that represents the paper size and printing area for the print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printPaper: UIPrintPaper? { get }
```

#### Discussion

`UIPrintInteractionController` sets this property immediately after the user selects a printer and before it calls the delegate’s [`printInteractionControllerWillStartJob(_:)`](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:).md) method. If its delegate implements the [`printInteractionController(_:choosePaper:)`](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosepaper:).md) method of the `UIPrintInteractionControllerDelegate` protocol, it can return the [`UIPrintPaper`](uiprintpaper.md) object to assign to this property. Otherwise, UIKit assigns an object with a default paper size and printing rectangle that is based on the output type and the capabilities of the destination printer. This object is released when the print job finishes.

## See Also

- [var printInfo: UIPrintInfo?](uiprintinteractioncontroller/printinfo.md)
  An object that encapsulates information about the print job.
- [var showsNumberOfCopies: Bool](uiprintinteractioncontroller/showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperSelectionForLoadedPapers: Bool](uiprintinteractioncontroller/showspaperselectionforloadedpapers.md)
  A Boolean value that determines whether the paper selection menu displays.
- [var showsPaperOrientation: Bool](uiprintinteractioncontroller/showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.
- [var showsPageRange: Bool](uiprintinteractioncontroller/showspagerange.md)
  A Boolean value that determines whether the printing options include a page-range control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printpaper)*