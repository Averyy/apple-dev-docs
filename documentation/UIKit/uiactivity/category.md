# UIActivity.Category

**Framework**: UIKit  
**Kind**: enum

An enumeration that defines categories of activities.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Category
```

#### Overview

Activities have a defined category, and the activity UI may show activities grouped by category.

## Topics

### Constants
- [UIActivity.Category.action](uiactivity/category/action.md)
  Activities whose primary purpose is to take an action on the selected item, like copying an image or saving it to the camera roll.
- [UIActivity.Category.share](uiactivity/category/share.md)
  Activities whose primary purpose is to share the selected item, like sending an image by email.
### Initializers
- [init?(rawValue: Int)](uiactivity/category/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var activityCategory: UIActivity.Category](uiactivity/activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [var activityType: UIActivity.ActivityType?](uiactivity/activitytype-swift.property.md)
  The type of service being provided.
- [UIActivity.ActivityType](uiactivity/activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityTitle: String?](uiactivity/activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](uiactivity/activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/category)*