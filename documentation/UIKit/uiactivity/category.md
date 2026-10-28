# UIActivity.Category

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIActivityCategory : NSInteger;
```

## Overview

Activities have a defined category, and the activity UI may show activities grouped by category.

## Topics

### Constants
- [UIActivity.Category.action](./category/action.md)
  Activities whose primary purpose is to take an action on the selected item, like copying an image or saving it to the camera roll.
- [UIActivity.Category.share](./category/share.md)
  Activities whose primary purpose is to share the selected item, like sending an image by email.
### Initializers
- [init?(rawValue: Int)](./category/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the activity information
- [class var activityCategory: UIActivity.Category](./activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [var activityType: UIActivity.ActivityType?](./activitytype-swift.property.md)
  The type of service being provided.
- [UIActivity.ActivityType](./activitytype-swift.struct.md)
  A structure that describes the types of activities for which the system has built-in support.
- [var activityTitle: String?](./activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](./activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/category)*