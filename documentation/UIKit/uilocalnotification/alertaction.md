# alertAction

**Framework**: UIKit  
**Kind**: property

The title of the action button or slider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var alertAction: String? { get set }
```

#### Discussion

Assign a string or, preferably, a localized-string key (using [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString)) as the value. The alert action is the title of the right button of the alert or the value of the unlock slider, where the value replaces “unlock” in “slide to unlock”. If you specify `nil`, and [`alertBody`](uilocalnotification/alertbody.md) is non-`nil`, “View” (localized to the preferred language) is used as the default value.

## See Also

- [var alertBody: String?](uilocalnotification/alertbody.md)
  The message displayed in the notification alert.
- [var alertTitle: String?](uilocalnotification/alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](uilocalnotification/hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var alertLaunchImage: String?](uilocalnotification/alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](uilocalnotification/category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/alertaction)*