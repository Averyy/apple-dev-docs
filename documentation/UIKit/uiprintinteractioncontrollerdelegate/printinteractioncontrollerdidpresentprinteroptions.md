# printInteractionControllerDidPresentPrinterOptions(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the device has presented the printing-options user interface.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionControllerDidPresentPrinterOptions(_ printInteractionController: UIPrintInteractionController)
```

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.

## See Also

- [func printInteractionControllerWillPresentPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillpresentprinteroptions(_:).md)
  Tells the delegate that the device is about to display the printing-options user interface.
- [func printInteractionControllerWillDismissPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwilldismissprinteroptions(_:).md)
  Tells the delegate that the device is about to dismiss the printing-options user interface.
- [func printInteractionControllerDidDismissPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(_:).md)
  Tells the delegate that the device is dismissing the printing-options user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidpresentprinteroptions(_:))*