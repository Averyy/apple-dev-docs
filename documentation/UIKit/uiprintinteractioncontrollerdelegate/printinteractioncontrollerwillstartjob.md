# printInteractionControllerWillStartJob(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the print job is about to start.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionControllerWillStartJob(_ printInteractionController: UIPrintInteractionController)
```

#### Discussion

You can implement this method to do set-up tasks related to the print job. For example, an application that needs to do intensive rendering could implement this method to pause animations. This method is called before drawing begins but after the printing user interface is dismissed.

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.

## See Also

- [func printInteractionControllerDidDismissPrinterOptions(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerdiddismissprinteroptions(_:).md)
  Tells the delegate that the device is dismissing the printing-options user interface.
- [func printInteractionControllerDidFinishJob(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidfinishjob(_:).md)
  Tells the delegate that the print job has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:))*