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

- **activityType**: The type of the service that was selected by the user. For custom services, this is the value returned by the [`activityType`](uiactivity/activitytype-swift.property.md) method of a [`UIActivity`](uiactivity.md) object. For system-defined activities, it is one of the strings listed in “Built-in Activity Types” in [`UIActivity`](uiactivity.md).
- **completed**: [`true`](https://developer.apple.com/documentation/Swift/true) if the service was performed or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not. This parameter is also set to [`false`](https://developer.apple.com/documentation/Swift/false) when the user dismisses the view controller without selecting a service.
- **returnedItems**: An array of [`NSExtensionItem`](https://developer.apple.com/documentation/Foundation/NSExtensionItem) objects containing any modified data. Use the items in this array to get any changes made to the original data by an extension. If no items were modified, the value of this parameter is `nil`.
- **activityError**: An error object if the activity failed to complete, or `nil` if the the activity completed normally.

## See Also

- [var completionWithItemsHandler: UIActivityViewController.CompletionWithItemsHandler?](uiactivityviewcontroller/completionwithitemshandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.typealias)*