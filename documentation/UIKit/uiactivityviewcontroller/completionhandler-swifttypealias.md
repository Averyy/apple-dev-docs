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

- **activityType**: The type of the service that was selected by the user. For custom services, this is the value returned by the [`activityType`](uiactivity/activitytype-swift.property.md) method of a [`UIActivity`](uiactivity.md) object. For system-defined activities, it is one of the strings listed in “Built-in Activity Types” in [`UIActivity`](uiactivity.md).
- **completed**: [`true`](https://developer.apple.com/documentation/swift/true) if the service was performed or [`false`](https://developer.apple.com/documentation/swift/false) if it was not. This parameter is also set to [`false`](https://developer.apple.com/documentation/swift/false) when the user dismisses the view controller without selecting a service.

## See Also

- [var completionHandler: UIActivityViewController.CompletionHandler?](uiactivityviewcontroller/completionhandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.typealias)*