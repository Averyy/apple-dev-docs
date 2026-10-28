# alertAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The title of the action button or slider.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var alertAction: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * alertAction;
```

## Discussion

Assign a string or, preferably, a localized-string key (using [`NSLocalizedString`](../../Foundation/nslocalizedstring.md)) as the value. The alert action is the title of the right button of the alert or the value of the unlock slider, where the value replaces “unlock” in “slide to unlock”. If you specify `nil`, and [`alertBody`](./alertbody.md) is non-`nil`, “View” (localized to the preferred language) is used as the default value.

## See Also

### Composing the alert
- [var alertBody: String?](./alertbody.md)
  The message displayed in the notification alert.
- [var alertTitle: String?](./alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](./hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var alertLaunchImage: String?](./alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](./category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/alertaction)*