# didSelectCancel()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Sent to the compose view after the cancel animation finishes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
func didSelectCancel()
```

```objc
- (void) didSelectCancel;
```

## Discussion

By default, this method calls the completeRequestReturningItems: method of the associated [`extensionContext`](../../UIKit/uiviewcontroller/extensioncontext.md) property, passing the appropriate error value in the `items` array and a `nil` expiration.

## See Also

### Responding to Lifecycle Events
- [func presentationAnimationDidFinish()](./presentationanimationdidfinish%28%29.md)
  Tells the compose view controller that the presentation animation is finished.
- [func didSelectPost()](./didselectpost%28%29.md)
  Sent to the compose view after the post animation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/didselectcancel())*