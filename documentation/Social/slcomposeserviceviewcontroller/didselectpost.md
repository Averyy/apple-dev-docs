# didSelectPost()

**Framework**: Social  
**Kind**: method

Sent to the compose view after the post animation finishes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
func didSelectPost()
```

#### Discussion

By default, this method calls the completeRequestReturningItems: method of the associated [`extensionContext`](https://developer.apple.com/documentation/UIKit/UIViewController/extensionContext) property, passing `nil` in the `items` array and a `nil` expiration handler. You must override `didSelectPost` to perform the post of [`contentText`](slcomposeserviceviewcontroller/contenttext.md) and any attachments. In your implementation of this method, you can call `super` to take advantage of the default completion handler; if you don’t call `super`, you must call the completion method of the extension context.

## See Also

- [func presentationAnimationDidFinish()](slcomposeserviceviewcontroller/presentationanimationdidfinish.md)
  Tells the compose view controller that the presentation animation is finished.
- [func didSelectCancel()](slcomposeserviceviewcontroller/didselectcancel.md)
  Sent to the compose view after the cancel animation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/didselectpost())*