# userInfo

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A dictionary for passing custom information to the notified app.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary * userInfo;
```

#### Discussion

You may add arbitrary key-value pairs to this dictionary. However, the keys and values must be valid [Property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44); if any are not, an exception is raised.

## See Also

### Configuring other parts of the notification
- [var applicationIconBadgeNumber: Int](./applicationiconbadgenumber.md)
  The number to display as the app’s icon badge.
- [var soundName: String?](./soundname.md)
  The name of the file containing the sound to play when an alert is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/userinfo)*