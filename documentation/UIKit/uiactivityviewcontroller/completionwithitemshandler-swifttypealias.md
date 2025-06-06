# UIActivityViewController.CompletionWithItemsHandler

**Framework**: UIKit  
**Kind**: typealias

A completion handler to execute after the activity view controller is dismissed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
typealias CompletionWithItemsHandler = (UIActivity.ActivityType?, Bool, [Any]?, (any Error)?) -> Void
```

#### Discussion

Upon the completion of an activity, or the dismissal of the activity view controller, the view controller’s completion block is executed. You can use this block to execute any final code related to the service. The parameters of this block are as follows:

## See Also

- [var completionWithItemsHandler: UIActivityViewController.CompletionWithItemsHandler?](uiactivityviewcontroller/completionwithitemshandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.typealias)*