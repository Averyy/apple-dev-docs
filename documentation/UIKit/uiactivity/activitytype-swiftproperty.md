# activityType

**Framework**: UIKit  
**Kind**: property

The type of service being provided.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var activityType: UIActivity.ActivityType? { get }
```

#### Discussion

The default value is `nil`. Subclasses may override this property to return a custom activity type that’s reported to the [`completionWithItemsHandler`](uiactivityviewcontroller/completionwithitemshandler-swift.property.md) completion handler.

## See Also

- [class var activityCategory: UIActivity.Category](uiactivity/activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [UIActivity.Category](uiactivity/category.md)
  An enumeration that defines categories of activities.
- [UIActivity.ActivityType](uiactivity/activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityTitle: String?](uiactivity/activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](uiactivity/activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.property)*