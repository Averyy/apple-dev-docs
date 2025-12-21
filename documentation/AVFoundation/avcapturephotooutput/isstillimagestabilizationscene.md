# isStillImageStabilizationScene

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the scene currently being previewed by the camera warrants image stabilization.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isStillImageStabilizationScene: Bool { get }
```

#### Discussion

This property’s value changes depending on the scene currently visible to the camera. For example, you might use this property to highlight  controls in your app’s camera UI related to image stabilization, indicating to the user that the scene is dark enough that enabling image stabilization might be desirable.

If the photo capture output’s [`isStillImageStabilizationSupported`](avcapturephotooutput/isstillimagestabilizationsupported.md) value is [`false`](https://developer.apple.com/documentation/Swift/false), this property’s value is always [`false`](https://developer.apple.com/documentation/Swift/false).

This property supports key-value observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationscene)*