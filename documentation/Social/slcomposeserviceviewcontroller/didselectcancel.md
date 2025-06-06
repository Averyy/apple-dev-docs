# didSelectCancel()

**Framework**: Social  
**Kind**: method

Sent to the compose view after the cancel animation finishes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
func didSelectCancel()
```

#### Discussion

By default, this method calls the completeRequestReturningItems: method of the associated [`extensionContext`](https://developer.apple.com/documentation/UIKit/UIViewController/extensionContext) property, passing the appropriate error value in the `items` array and a `nil` expiration.

## See Also

- [func presentationAnimationDidFinish()](slcomposeserviceviewcontroller/presentationanimationdidfinish.md)
  Tells the compose view controller that the presentation animation is finished.
- [func didSelectPost()](slcomposeserviceviewcontroller/didselectpost.md)
  Sent to the compose view after the post animation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/didselectcancel())*