# show(withTitle:message:duration:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Displays a banner to the player for a specified period of time.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func show(withTitle title: String?, message: String?, duration: TimeInterval) async
```

## Parameters

- `title`: The title of the banner.
- `message`: The message on the banner.
- `duration`: The amount of time that GameKit should dispay the banner to the player.
- `completionHandler`: The block that GameKit calls when the player or GameKit dismisses the banner.

## See Also

- [class func show(withTitle: String?, message: String?, completionHandler: (() -> Void)?)](gknotificationbanner/show(withtitle:message:completionhandler:).md)
  Displays a banner with a title and message to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gknotificationbanner/show(withtitle:message:duration:completionhandler:))*