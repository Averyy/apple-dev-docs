# alertBody

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The message displayed in the notification alert.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var alertBody: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * alertBody;
```

#### Discussion

Assign a string or, preferably, a localized-string key (using [`NSLocalizedString`](../../Foundation/nslocalizedstring.md)) as the value of the message. If the value of this property is non-`nil`, an alert is displayed. The default value is `nil` (no alert). Printf style escape characters are stripped from the string prior to display; to include a percent symbol (%) in the message, use two percent symbols (%%).

## See Also

### Composing the alert
- [var alertAction: String?](./alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](./alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](./hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var alertLaunchImage: String?](./alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](./category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/alertbody)*