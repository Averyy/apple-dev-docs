# printInteractionControllerWillDismissPrinterOptions(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the device is about to dismiss the printing-options user interface.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func printInteractionControllerWillDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)
```

```objc
- (void) printInteractionControllerWillDismissPrinterOptions:(UIPrintInteractionController *) printInteractionController;
```

## Parameters

- `printInteractionController`: The shared instance of [`UIPrintInteractionController`](../uiprintinteractioncontroller.md) that is managing the print job.

## See Also

### Responding to the Presentation and Dismissal of the Printing Interface
- [func printInteractionControllerWillPresentPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerwillpresentprinteroptions%28_%29.md)
  Tells the delegate that the device is about to display the printing-options user interface.
- [func printInteractionControllerDidPresentPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerdidpresentprinteroptions%28_%29.md)
  Tells the delegate that the device has presented the printing-options user interface.
- [func printInteractionControllerDidDismissPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerdiddismissprinteroptions%28_%29.md)
  Tells the delegate that the device is dismissing the printing-options user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerwilldismissprinteroptions(_:))*