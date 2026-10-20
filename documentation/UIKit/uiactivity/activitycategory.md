# activityCategory

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, readonly) UIActivityCategory activityCategory;
```

#### Return Value

The assigned category of the activity. The default implementation returns [`UIActivity.Category.action`](./category/action.md).

#### Discussion

Override this property to define a different activity category for your custom activity.

## See Also

### Getting the activity information
- [UIActivity.Category](./category.md)
  An enumeration that defines categories of activities.
- [var activityType: UIActivity.ActivityType?](./activitytype-swift.property.md)
  The type of service being provided.
- [UIActivity.ActivityType](./activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityTitle: String?](./activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](./activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitycategory)*