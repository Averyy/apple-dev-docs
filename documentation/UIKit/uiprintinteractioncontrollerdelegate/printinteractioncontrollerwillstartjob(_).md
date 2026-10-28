# printInteractionControllerWillStartJob(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the print job is about to start.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func printInteractionControllerWillStartJob(_ printInteractionController: UIPrintInteractionController)
```

```objc
- (void) printInteractionControllerWillStartJob:(UIPrintInteractionController *) printInteractionController;
```

## Discussion

You can implement this method to do set-up tasks related to the print job. For example, an application that needs to do intensive rendering could implement this method to pause animations. This method is called before drawing begins but after the printing user interface is dismissed.

## Parameters

- `printInteractionController`: The shared instance of [`UIPrintInteractionController`](../uiprintinteractioncontroller.md) that is managing the print job.

## See Also

### Related Documentation
- [func printInteractionControllerDidDismissPrinterOptions(UIPrintInteractionController)](./printinteractioncontrollerdiddismissprinteroptions%28_%29.md)
  Tells the delegate that the device is dismissing the printing-options user interface.
### Responding to the Start and End of a Print Job
- [func printInteractionControllerDidFinishJob(UIPrintInteractionController)](./printinteractioncontrollerdidfinishjob%28_%29.md)
  Tells the delegate that the print job has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:))*