# UIActivityViewController.CompletionHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A completion handler to execute after the activity view controller is dismissed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

> **Deprecated**: Use [`UIActivityViewController.CompletionWithItemsHandler`](./completionwithitemshandler-swift.typealias.md) instead.

## Declaration

```swift
typealias CompletionHandler = (UIActivity.ActivityType?, Bool) -> Void
```

```c
typedef void (^)(NSString *, _Bool) UIActivityViewControllerCompletionHandler;
```

#### Discussion

Upon the completion of an activity, or the dismissal of the activity view controller, the view controller’s completion block is executed. You can use this block to execute any final code related to the service. The parameters of this block are as follows:

- **activityType**: The type of the service that was selected by the user. For custom services, this is the value returned by the [`activityType`](../uiactivity/activitytype-swift.property.md) method of a [`UIActivity`](../uiactivity.md) object. For system-defined activities, it is one of the strings listed in “Built-in Activity Types” in [`UIActivity`](../uiactivity.md).
- **completed**: [`true`](../../Swift/true.md) if the service was performed or [`false`](../../Swift/false.md) if it was not. This parameter is also set to [`false`](../../Swift/false.md) when the user dismisses the view controller without selecting a service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.typealias)*