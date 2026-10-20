# category

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The name of the action group that corresponds to this notification.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var category: String? { get set }
```

```objc
@property (copy, nullable) NSString * category;
```

#### Discussion

Categories allow you to present custom actions to the user on your push notifications. For more information, see [`UIMutableUserNotificationCategory`](../../../UIKit/uimutableusernotificationcategory.md).

## See Also

### Grouping Notifications
- [var collapseIDKey: String?](./collapseidkey.md)
  A value that the system uses to coalesce unseen push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/category)*