# alertLaunchImage

**Framework**: UIKit  
**Kind**: property

Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var alertLaunchImage: String? { get set }
```

#### Discussion

The string is a filename of an image file in the app bundle. This image is a launching image specified for a given notification; when the user taps the action button (for example, “View”) or moves the action slider, the image is used in place of the default launching image. If the value of this property is `nil` (the default), the system either uses the previous snapshot, uses the image identified by the `UILaunchImageFile` key in the app’s `Info.plist` file, or falls back to `Default.png`.

The value of this key has the exact same semantics as `UILaunchImageFile`. For more about this key, see the [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

## See Also

- [var alertBody: String?](uilocalnotification/alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](uilocalnotification/alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](uilocalnotification/alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](uilocalnotification/hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var category: String?](uilocalnotification/category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/alertlaunchimage)*