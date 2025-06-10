# SLComposeViewControllerResult

**Framework**: Social  
**Kind**: enum

Possible values for the `result` parameter of the [`completionHandler`](slcomposeviewcontroller/completionhandler.md) property.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+

## Declaration

```swift
enum SLComposeViewControllerResult
```

## Topics

### Constants
- [SLComposeViewControllerResult.cancelled](slcomposeviewcontrollerresult/cancelled.md)
  The view controller is dismissed without sending the post.
- [SLComposeViewControllerResult.done](slcomposeviewcontrollerresult/done.md)
  The view controller is dismissed and the message is being sent in the background.
### Initializers
- [init?(rawValue: Int)](slcomposeviewcontrollerresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var completionHandler: SLComposeViewControllerCompletionHandler!](slcomposeviewcontroller/completionhandler.md)
  The handler to call when the user is done composing a post.
- [typealias SLComposeViewControllerCompletionHandler](slcomposeviewcontrollercompletionhandler.md)
  Defines a handler to call when the user finishes composing a post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontrollerresult)*