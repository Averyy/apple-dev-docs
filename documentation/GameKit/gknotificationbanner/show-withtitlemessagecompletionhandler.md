# show(withTitle:message:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Displays a banner with a title and message to the player.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func show(withTitle title: String?, message: String?) async
```

## Parameters

- `title`: The title of the banner.
- `message`: The message on the banner.
- `completionHandler`: The block that GameKit calls when the player dismisses the banner.

## See Also

- [class func show(withTitle: String?, message: String?, duration: TimeInterval, completionHandler: (() -> Void)?)](gknotificationbanner/show(withtitle:message:duration:completionhandler:).md)
  Displays a banner to the player for a specified period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gknotificationbanner/show(withtitle:message:completionhandler:))*