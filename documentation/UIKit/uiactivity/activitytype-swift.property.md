# activityType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) UIActivityType activityType;
```

## Discussion

The default value is `nil`. Subclasses may override this property to return a custom activity type that’s reported to the [`completionWithItemsHandler`](../uiactivityviewcontroller/completionwithitemshandler-swift.property.md) completion handler.

## See Also

### Getting the activity information
- [class var activityCategory: UIActivity.Category](./activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [UIActivity.Category](./category.md)
  An enumeration that defines categories of activities.
- [UIActivity.ActivityType](./activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityTitle: String?](./activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](./activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.property)*