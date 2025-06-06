# category

**Framework**: UIKit  
**Kind**: property

The name of a group of actions to display in the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var category: String? { get set }
```

#### Discussion

The value of this property is the category name associated with a registered [`UIUserNotificationSettings`](uiusernotificationsettings.md) object. When the alert for the local notification is displayed, the system uses the string you specify to look up the group and retrieve its actions. It then adds a button to the alert for each action defined by the group. When the user taps one of those buttons, the app is woken up (or launched) and given a chance to perform the designated action. If the specified category name does not belong to a registered group of actions, the alert does not display any additional action buttons.

Specifying custom actions is optional. The value of this property is `nil` by default.

## See Also

- [var alertBody: String?](uilocalnotification/alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](uilocalnotification/alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](uilocalnotification/alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](uilocalnotification/hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var alertLaunchImage: String?](uilocalnotification/alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/category)*