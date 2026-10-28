# SLComposeViewControllerCompletionHandler

**Framework**: Social  
**Kind**: typealias  
**Role**: Type Alias

Defines a handler to call when the user finishes composing a post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+

## Declaration

```swift
typealias SLComposeViewControllerCompletionHandler = (SLComposeViewControllerResult) -> Void
```

```c
typedef void (^)(enum SLComposeViewControllerResult) SLComposeViewControllerCompletionHandler;
```

## Discussion

The completion handler is called while the SLComposeViewController is still visible and it is responsible for dismissing the view controller. For the possible values of the `result` parameter, see [`SLComposeViewControllerResult`](./slcomposeviewcontrollerresult.md). Use the [`completionHandler`](./slcomposeviewcontroller/completionhandler.md) property to set this handler.

## See Also

### Processing the Results
- [var completionHandler: SLComposeViewControllerCompletionHandler!](./slcomposeviewcontroller/completionhandler.md)
  The handler to call when the user is done composing a post.
- [enum SLComposeViewControllerResult](./slcomposeviewcontrollerresult.md)
  Possible values for the `result` parameter of the [`completionHandler`](./slcomposeviewcontroller/completionhandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontrollercompletionhandler)*