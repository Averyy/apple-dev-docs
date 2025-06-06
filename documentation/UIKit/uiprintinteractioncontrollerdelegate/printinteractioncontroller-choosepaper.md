# printInteractionController(_:choosePaper:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for an object that encapsulates the paper size and printing area for the print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, choosePaper paperList: [UIPrintPaper]) -> UIPrintPaper
```

#### Return Value

A [`UIPrintPaper`](uiprintpaper.md) object representing both the paper size and imageable area (or printable rectangle) to use for the print job.

#### Discussion

This method is intended for apps (typically document-based apps) that have a notion of distinct paper sizes. The delegate can examine the objects in `paperList` to locate the paper size and printable rectangle combination that is best suited for its needs and return the encapsulating `UIPrintPaper` object. Or it can call the [`bestPaper(forPageSize:withPapersFrom:)`](uiprintpaper/bestpaper(forpagesize:withpapersfrom:).md) class method of the [`UIPrintPaper`](uiprintpaper.md) class, passing in a specific page size (typically the document size), and return the object returned by that method.

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.
- `paperList`: An array of   objects that represent combinations of paper sizes and imageable areas supported by the selected printer.

## See Also

- [var printPaper: UIPrintPaper?](uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [func printInteractionController(UIPrintInteractionController, cutLengthFor: UIPrintPaper) -> CGFloat](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:cutlengthfor:).md)
  Asks the delegate for a length to use when cutting the page.
- [func printInteractionController(UIPrintInteractionController, chooseCutterBehavior: [Any]) -> UIPrinter.CutterBehavior](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosecutterbehavior:).md)
  Asks the delegate for the cutter behavior for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosepaper:))*