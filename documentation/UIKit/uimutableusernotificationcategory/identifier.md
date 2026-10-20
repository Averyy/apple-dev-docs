# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The name of the action group.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIMutableUserNotificationCategory`](../uimutableusernotificationcategory.md).

## Declaration

```swift
var identifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * identifier;
```

#### Discussion

This property is a writable version of the one declared by the parent class.

When generating a notification that includes these custom actions, you must use this string to initialize the notification. For local notifications, assign the string to the [`category`](../uilocalnotification/category.md) property of the [`UILocalNotification`](../uilocalnotification.md) object. For push notifications, use the string as the value of the `category` key in the push notification’s payload.

## See Also

### Modifying the action settings
- [func setActions([UIUserNotificationAction]?, for: UIUserNotificationActionContext)](./setactions%28_,for%29.md)
  Sets the actions to display for different alert styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/identifier)*