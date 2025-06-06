# printInteractionControllerDidFinishJob(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the print job has ended.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printInteractionControllerDidFinishJob(_ printInteractionController: UIPrintInteractionController)
```

#### Discussion

You can implement this method to do clean-up tasks related to the print job. This method is called after the last page of the print job is generated but before the completion handler (a block handler of type [`UIPrintInteractionController.CompletionHandler`](uiprintinteractioncontroller/completionhandler.md)) is called.

## Parameters

- `printInteractionController`: The shared instance of   that is managing the print job.

## See Also

- [func printInteractionControllerWillStartJob(UIPrintInteractionController)](uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(_:).md)
  Tells the delegate that the print job is about to start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerdidfinishjob(_:))*