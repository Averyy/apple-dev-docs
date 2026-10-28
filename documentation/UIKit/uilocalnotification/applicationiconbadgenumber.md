# applicationIconBadgeNumber

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number to display as the app’s icon badge.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var applicationIconBadgeNumber: Int { get set }
```

```objc
@property (nonatomic) NSInteger applicationIconBadgeNumber;
```

## Discussion

The default value of this property is 0, which means that no badge is displayed.

## See Also

### Configuring other parts of the notification
- [var soundName: String?](./soundname.md)
  The name of the file containing the sound to play when an alert is displayed.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary for passing custom information to the notified app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/applicationiconbadgenumber)*