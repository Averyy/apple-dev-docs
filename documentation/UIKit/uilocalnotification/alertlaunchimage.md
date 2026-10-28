# alertLaunchImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: For more information, see [`UILocalNotification`](../uilocalnotification.md).

## Declaration

```swift
var alertLaunchImage: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * alertLaunchImage;
```

## Discussion

The string is a filename of an image file in the app bundle. This image is a launching image specified for a given notification; when the user taps the action button (for example, “View”) or moves the action slider, the image is used in place of the default launching image. If the value of this property is `nil` (the default), the system either uses the previous snapshot, uses the image identified by the `UILaunchImageFile` key in the app’s `Info.plist` file, or falls back to `Default.png`.

The value of this key has the exact same semantics as `UILaunchImageFile`. For more about this key, see the [Information Property List Key Reference](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

## See Also

### Composing the alert
- [var alertBody: String?](./alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](./alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](./alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](./hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var category: String?](./category.md)
  The name of a group of actions to display in the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/alertlaunchimage)*