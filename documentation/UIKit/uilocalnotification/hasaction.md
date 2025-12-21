# hasAction

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the notification shows or hides the alert action.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var hasAction: Bool { get set }
```

#### Discussion

Assign [`false`](https://developer.apple.com/documentation/Swift/false) to this property to hide the alert button or slider. (This effect requires [`alertBody`](uilocalnotification/alertbody.md) to be non-`nil`.) The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var alertBody: String?](uilocalnotification/alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](uilocalnotification/alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](uilocalnotification/alerttitle.md)
  A short description of the reason for the alert.
- [var alertLaunchImage: String?](uilocalnotification/alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](uilocalnotification/category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/hasaction)*