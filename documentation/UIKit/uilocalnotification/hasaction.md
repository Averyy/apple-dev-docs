# hasAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the notification shows or hides the alert action.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var hasAction: Bool { get set }
```

```objc
@property (nonatomic) BOOL hasAction;
```

## Discussion

Assign [`false`](../../Swift/false.md) to this property to hide the alert button or slider. (This effect requires [`alertBody`](./alertbody.md) to be non-`nil`.) The default value is [`true`](../../Swift/true.md).

## See Also

### Composing the alert
- [var alertBody: String?](./alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](./alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](./alerttitle.md)
  A short description of the reason for the alert.
- [var alertLaunchImage: String?](./alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](./category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/hasaction)*