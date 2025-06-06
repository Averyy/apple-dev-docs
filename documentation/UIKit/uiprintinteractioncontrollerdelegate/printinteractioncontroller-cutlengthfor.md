# printInteractionController(_:cutLengthFor:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a length to use when cutting the page.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, cutLengthFor paper: UIPrintPaper) -> CGFloat
```

#### Return Value

The physical length of the page in points.

#### Discussion

Some printers can cut a roll of print paper at a particular length. If you implement this method in your delegate, then it may be called during a print job. Your delegate should determine the length in which the content fits and return this value. When printed, the paper will be cut to this length.

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.
- `paper`: A   that specifies the maximum physical and printable areas of the page.

## See Also

- [func printInteractionController(UIPrintInteractionController, choosePaper: [UIPrintPaper]) -> UIPrintPaper](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosepaper:).md)
  Asks the delegate for an object that encapsulates the paper size and printing area for the print job.
- [func printInteractionController(UIPrintInteractionController, chooseCutterBehavior: [Any]) -> UIPrinter.CutterBehavior](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosecutterbehavior:).md)
  Asks the delegate for the cutter behavior for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:cutlengthfor:))*