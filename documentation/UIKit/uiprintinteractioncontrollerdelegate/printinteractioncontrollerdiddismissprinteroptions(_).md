# printInteractionControllerDidDismissPrinterOptions(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the device is dismissing the printing-options user interface.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func printInteractionControllerDidDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)
```

```objc
- (void) printInteractionControllerDidDismissPrinterOptions:(UIPrintInteractionController *) printInteractionController;
```

## Discussion

This message is sent both when the user taps Print on the printing-options view and when the user dismisses the view by tapping outside it.

## Parameters

- `printInteractionController`: The shared instance of [`UIPrintInteractionController`](../uiprintinteractioncontroller.md) that is managing the print job.

## See Also

### Responding to the Presentation and Dismissal of the Printing Interface
- [func printInteractionControllerWillPresentPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerwillpresentprinteroptions%28_%29.md)
  Tells the delegate that the device is about to display the printing-options user interface.
- [func printInteractionControllerDidPresentPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerdidpresentprinteroptions%28_%29.md)
  Tells the delegate that the device has presented the printing-options user interface.
- [func printInteractionControllerWillDismissPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerwilldismissprinteroptions%28_%29.md)
  Tells the delegate that the device is about to dismiss the printing-options user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(_:))*