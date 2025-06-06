# presentationAnimationDidFinish()

**Framework**: Social  
**Kind**: method

Tells the compose view controller that the presentation animation is finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
func presentationAnimationDidFinish()
```

#### Discussion

Implement this method to avoid performing lengthy work during initialization or the iOS view controller methods [`viewWillAppear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewWillAppear(_:)) and [`viewDidAppear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidAppear(_:)).

## See Also

- [func didSelectCancel()](slcomposeserviceviewcontroller/didselectcancel.md)
  Sent to the compose view after the cancel animation finishes.
- [func didSelectPost()](slcomposeserviceviewcontroller/didselectpost.md)
  Sent to the compose view after the post animation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/presentationanimationdidfinish())*