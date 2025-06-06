# UIActivityViewController.CompletionHandler

**Framework**: UIKit  
**Kind**: typealias

A completion handler to execute after the activity view controller is dismissed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
typealias CompletionHandler = (UIActivity.ActivityType?, Bool) -> Void
```

#### Discussion

Upon the completion of an activity, or the dismissal of the activity view controller, the view controller’s completion block is executed. You can use this block to execute any final code related to the service. The parameters of this block are as follows:

## See Also

- [var completionHandler: UIActivityViewController.CompletionHandler?](uiactivityviewcontroller/completionhandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.typealias)*