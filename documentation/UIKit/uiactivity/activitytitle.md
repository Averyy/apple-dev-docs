# activityTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSString * activityTitle;
```

#### Return Value

A string that describes the service.

#### Discussion

The default value is `nil`. Subclasses must override this property to return a user-readable string that describes the service. The string you return should be localized.

## See Also

### Getting the activity information
- [class var activityCategory: UIActivity.Category](./activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [UIActivity.Category](./category.md)
  An enumeration that defines categories of activities.
- [var activityType: UIActivity.ActivityType?](./activitytype-swift.property.md)
  The type of service being provided.
- [UIActivity.ActivityType](./activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityImage: UIImage?](./activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytitle)*