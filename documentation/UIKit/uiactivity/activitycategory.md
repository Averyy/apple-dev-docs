# activityCategory

**Framework**: UIKit  
**Kind**: property

The category of the activity, which may be used to group activities in the UI.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class var activityCategory: UIActivity.Category { get }
```

#### Return Value

The assigned category of the activity. The default implementation returns [`UIActivity.Category.action`](uiactivity/category/action.md).

#### Discussion

Override this property to define a different activity category for your custom activity.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitycategory)*