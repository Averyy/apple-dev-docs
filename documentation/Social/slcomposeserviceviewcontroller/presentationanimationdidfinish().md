# presentationAnimationDidFinish()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Tells the compose view controller that the presentation animation is finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
func presentationAnimationDidFinish()
```

```objc
- (void) presentationAnimationDidFinish;
```

#### Discussion

Implement this method to avoid performing lengthy work during initialization or the iOS view controller methods [`viewWillAppear(_:)`](../../UIKit/uiviewcontroller/viewwillappear%28_%29.md) and [`viewDidAppear(_:)`](../../UIKit/uiviewcontroller/viewdidappear%28_%29.md).

## See Also

### Responding to Lifecycle Events
- [func didSelectCancel()](./didselectcancel%28%29.md)
  Sent to the compose view after the cancel animation finishes.
- [func didSelectPost()](./didselectpost%28%29.md)
  Sent to the compose view after the post animation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/presentationanimationdidfinish())*