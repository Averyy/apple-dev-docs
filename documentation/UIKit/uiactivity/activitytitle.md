# activityTitle

**Framework**: UIKit  
**Kind**: property

A user-readable string that describes the service.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var activityTitle: String? { get }
```

#### Return Value

A string that describes the service.

#### Discussion

The default value is `nil`. Subclasses must override this property to return a user-readable string that describes the service. The string you return should be localized.

## See Also

- [class var activityCategory: UIActivity.Category](uiactivity/activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [UIActivity.Category](uiactivity/category.md)
  An enumeration that defines categories of activities.
- [var activityType: UIActivity.ActivityType?](uiactivity/activitytype-swift.property.md)
  The type of service being provided.
- [UIActivity.ActivityType](uiactivity/activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityImage: UIImage?](uiactivity/activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytitle)*