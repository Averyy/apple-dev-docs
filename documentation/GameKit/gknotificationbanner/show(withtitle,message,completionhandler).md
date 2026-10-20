# show(withTitle:message:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Displays a banner with a title and message to the player.

**Availability**:
- iOS 5.0+ - Deprecated in 16.1
- iPadOS 5.0+ - Deprecated in 16.1
- Mac Catalyst 13.1+ - Deprecated in 16.1
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`UNNotificationRequest`](../../UserNotifications/unnotificationrequest.md) or provide a custom interface instead.

## Declaration

```swift
class func show(withTitle title: String?, message: String?, completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
class func show(withTitle title: String?, message: String?) async
```

```objc
+ (void) showBannerWithTitle:(NSString *) title message:(NSString *) message completionHandler:(void (^)()) completionHandler;
```

## Parameters

- `title`: The title of the banner.
- `message`: The message on the banner.
- `completionHandler`: The block that GameKit calls when the player dismisses the banner.

## See Also

### Displaying the Banner
- [class func show(withTitle: String?, message: String?, duration: TimeInterval, completionHandler: (() -> Void)?)](./show%28withtitle,message,duration,completionhandler%29.md)
  Displays a banner to the player for a specified period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gknotificationbanner/show(withtitle:message:completionhandler:))*