# alertTitle

**Framework**: UIKit  
**Kind**: property

A short description of the reason for the alert.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var alertTitle: String? { get set }
```

#### Discussion

Use this property to provide a short description of the reason for the alert. You may specify a string with the text you want to display or you may specify a string to use as a lookup key in your app’s `Localizable.strings` file. The default value of this property is `nil`.

Title strings should be short, usually only a couple of words describing the reason for the notification. Apple Watch displays the title string as part of the short look notification interface, which has limited space.

## See Also

- [var alertBody: String?](uilocalnotification/alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](uilocalnotification/alertaction.md)
  The title of the action button or slider.
- [var hasAction: Bool](uilocalnotification/hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var alertLaunchImage: String?](uilocalnotification/alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](uilocalnotification/category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/alerttitle)*