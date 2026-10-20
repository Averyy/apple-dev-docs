# printInteractionController(_:cutLengthFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a length to use when cutting the page.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, cutLengthFor paper: UIPrintPaper) -> CGFloat
```

```objc
- (CGFloat) printInteractionController:(UIPrintInteractionController *) printInteractionController cutLengthForPaper:(UIPrintPaper *) paper;
```

#### Return Value

The physical length of the page in points.

#### Discussion

Some printers can cut a roll of print paper at a particular length. If you implement this method in your delegate, then it may be called during a print job. Your delegate should determine the length in which the content fits and return this value. When printed, the paper will be cut to this length.

## Parameters

- `printInteractionController`: The shared instance of [`UIPrintInteractionController`](../uiprintinteractioncontroller.md) that is managing the print job.
- `paper`: A [`UIPrintPaper`](../uiprintpaper.md) that specifies the maximum physical and printable areas of the page.

## See Also

### Choosing a Paper Size for the Print Job
- [func printInteractionController(UIPrintInteractionController, choosePaper: [UIPrintPaper]) -> UIPrintPaper](./printinteractioncontroller%28_,choosepaper%29.md)
  Asks the delegate for an object that encapsulates the paper size and printing area for the print job.
- [func printInteractionController(UIPrintInteractionController, chooseCutterBehavior: [Any]) -> UIPrinter.CutterBehavior](./printinteractioncontroller%28_,choosecutterbehavior%29.md)
  Asks the delegate for the cutter behavior for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:cutlengthfor:))*