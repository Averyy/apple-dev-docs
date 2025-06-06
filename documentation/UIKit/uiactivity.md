# UIActivity

**Framework**: UIKit  
**Kind**: class

An abstract class that you subclass to implement app-specific services.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class UIActivity
```

## Mentions

- [Adding custom actions and activities](adding-custom-actions-and-activities.md)

#### Overview

You should subclass [`UIActivity`](uiactivity.md) only if you want to provide custom services to people. A service takes data that’s passed to it, does something to that data, and returns the results. For example, a social media service might take whatever text, images, or other content is provided to it and post them to a person’s account. Activity objects are used in conjunction with a [`UIActivityViewController`](uiactivityviewcontroller.md) object, which is responsible for presenting services to people.

The system already provides support for many standard services and makes them available through the [`UIActivityViewController`](uiactivityviewcontroller.md) object. For example, the standard activity view controller supports emailing data, posting items to one of a person’s social media accounts, and several other options. You don’t have to provide custom services for any of the built-in types.

##### Subclassing Notes

This class must be subclassed before it can be used. The job of an activity object is to act on the data provided to it and to provide some meta information that iOS can display to people. For more complex services, an activity object can also display a custom user interface and use it to gather additional information from people.

###### Methods to Override

When subclassing, you must always override the following methods and use them to provide information about your service:

- [`activityType`](uiactivity/activitytype-swift.property.md)
- [`activityTitle`](uiactivity/activitytitle.md)
- [`activityImage`](uiactivity/activityimage.md)
- [`canPerform(withActivityItems:)`](uiactivity/canperform(withactivityitems:).md)
- [`prepare(withActivityItems:)`](uiactivity/prepare(withactivityitems:).md)
- [`activityCategory`](uiactivity/activitycategory.md)

If your [`canPerform(withActivityItems:)`](uiactivity/canperform(withactivityitems:).md) method indicates that your subclass is able to operate on the specified data, the active [`UIActivityViewController`](uiactivityviewcontroller.md) object displays your service to people. When a person selects your service, the activity view controller calls the [`prepare(withActivityItems:)`](uiactivity/prepare(withactivityitems:).md) method followed by only one of these methods:

- [`activityViewController`](uiactivity/activityviewcontroller.md) — Returns a view controller to present to a person. If your service requires additional input from a person, override this method and use it to return the view controller object responsible for presenting your custom UI. (You don’t need to present the view controller yourself.) After your view controller object gathers the needed input, it’s responsible for initiating the task associated with the service.
- [`perform()`](uiactivity/perform().md) — Performs the service without displaying any additional UI. If your service doesn’t need additional input from a person, override this method and perform the task associated with the service.

## Topics

### Getting the activity information
- [class var activityCategory: UIActivity.Category](uiactivity/activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [UIActivity.Category](uiactivity/category.md)
  An enumeration that defines categories of activities.
- [var activityType: UIActivity.ActivityType?](uiactivity/activitytype-swift.property.md)
  The type of service being provided.
- [UIActivity.ActivityType](uiactivity/activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityTitle: String?](uiactivity/activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](uiactivity/activityimage.md)
  An image that identifies the service to the user.
### Performing the activity
- [func canPerform(withActivityItems: [Any]) -> Bool](uiactivity/canperform(withactivityitems:).md)
  Queries whether the service can act on the specified data items.
- [func prepare(withActivityItems: [Any])](uiactivity/prepare(withactivityitems:).md)
  Prepares your service to act on the specified data.
- [var activityViewController: UIViewController?](uiactivity/activityviewcontroller.md)
  The view controller to present to the user.
- [func perform()](uiactivity/perform.md)
  Performs the service when no custom view controller is provided.
- [func activityDidFinish(Bool)](uiactivity/activitydidfinish(_:).md)
  Notifies the system that your activity object has completed its work.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIActivityViewController](uiactivityviewcontroller.md)
  A view controller that you use to offer standard services from your app.
- [protocol UIActivityItemSource](uiactivityitemsource.md)
  A set of methods that an activity view controller uses to retrieve the data items to act on.
- [class UIActivityItemProvider](uiactivityitemprovider.md)
  A proxy for data that passes to an activity view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity)*