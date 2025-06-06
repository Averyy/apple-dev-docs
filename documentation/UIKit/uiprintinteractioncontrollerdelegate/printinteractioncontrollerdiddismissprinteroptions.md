# printInteractionControllerDidDismissPrinterOptions(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the device is dismissing the printing-options user interface.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionControllerDidDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)
```

#### Discussion

This message is sent both when the user taps Print on the printing-options view and when the user dismisses the view by tapping outside it.

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.

## See Also

- [func printInteractionControllerWillPresentPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillpresentprinteroptions(_:).md)
  Tells the delegate that the device is about to display the printing-options user interface.
- [func printInteractionControllerDidPresentPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidpresentprinteroptions(_:).md)
  Tells the delegate that the device has presented the printing-options user interface.
- [func printInteractionControllerWillDismissPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwilldismissprinteroptions(_:).md)
  Tells the delegate that the device is about to dismiss the printing-options user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(_:))*