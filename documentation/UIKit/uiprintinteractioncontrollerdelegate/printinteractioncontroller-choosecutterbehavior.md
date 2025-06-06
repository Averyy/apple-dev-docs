# printInteractionController(_:chooseCutterBehavior:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the cutter behavior for the print job.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, chooseCutterBehavior availableBehaviors: [Any]) -> UIPrinter.CutterBehavior
```

#### Return Value

The cutter behavior to use for the print job. The value must correspond to one of the constants in the `availableBehaviors` parameter.

#### Discussion

Some roll-fed printers support different options for cutting the paper. If you implement this method in your delegate, then it may be called during a print job. Your delegate method should determine when to make cuts and return the appropriate value.

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.
- `availableBehaviors`: An array of   objects identifying the printer’s available cutter behaviors. Each number corresponds to one of the constants defined in  .

## See Also

- [func printInteractionController(UIPrintInteractionController, choosePaper: [UIPrintPaper]) -> UIPrintPaper](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosepaper:).md)
  Asks the delegate for an object that encapsulates the paper size and printing area for the print job.
- [func printInteractionController(UIPrintInteractionController, cutLengthFor: UIPrintPaper) -> CGFloat](uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:cutlengthfor:).md)
  Asks the delegate for a length to use when cutting the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosecutterbehavior:))*