# UIActivityItemProvider

**Framework**: UIKit  
**Kind**: class

A proxy for data that passes to an activity view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class UIActivityItemProvider
```

#### Overview

You can use a provider object in situations where you want to make data available for use by an activity but you want to delay providing that data until it’s actually needed. For example, you might use a provider object to represent a large video file that needs to be processed before it can be shared to a user’s social media account.

When you initialize a [`UIActivityViewController`](uiactivityviewcontroller.md) object, you can pass a provider object in addition to any other data objects. When the user selects an activity, the activity view controller adds your provider object (which is also an operation object) to an operation queue so that it can begin to gather or process the needed data.

##### Subclassing Notes

You must subclass `UIActivityItemProvider` and implement its [`item`](uiactivityitemprovider/item.md) method, which is called to generate the item data. You implement this method instead of the normal [`main()`](https://developer.apple.com/documentation/foundation/operation/1407732-main) method you’d implement for an operation object. (The [`main()`](https://developer.apple.com/documentation/foundation/operation/1407732-main) method calls the [`item`](uiactivityitemprovider/item.md) method when the operation object is executed.) Your implementation of the [`item`](uiactivityitemprovider/item.md) method should do whatever work is necessary to create and return the data.

## Topics

### Initializing the provider
- [init(placeholderItem: Any)](uiactivityitemprovider/init(placeholderitem:).md)
  Initializes and returns a provider object with the specified placeholder data.
### Accessing the provider attributes
- [var item: Any](uiactivityitemprovider/item.md)
  Generates and returns the actual data-bearing object.
- [var placeholderItem: Any?](uiactivityitemprovider/placeholderitem.md)
  The placeholder object you specified at initialization time.
- [var activityType: UIActivity.ActivityType?](uiactivityitemprovider/activitytype.md)
  The type of the activity object that is expecting the data.

## Relationships

### Inherits From
- [Operation](../Foundation/Operation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemSource](uiactivityitemsource.md)

## See Also

- [class UIActivity](uiactivity.md)
  An abstract class that you subclass to implement app-specific services.
- [class UIActivityViewController](uiactivityviewcontroller.md)
  A view controller that you use to offer standard services from your app.
- [protocol UIActivityItemSource](uiactivityitemsource.md)
  A set of methods that an activity view controller uses to retrieve the data items to act on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemprovider)*