# isStillImageStabilizationScene

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the scene currently being previewed by the camera warrants image stabilization.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var isStillImageStabilizationScene: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isStillImageStabilizationScene;
```

#### Discussion

This property’s value changes depending on the scene currently visible to the camera. For example, you might use this property to highlight  controls in your app’s camera UI related to image stabilization, indicating to the user that the scene is dark enough that enabling image stabilization might be desirable.

If the photo capture output’s [`isStillImageStabilizationSupported`](./isstillimagestabilizationsupported.md) value is [`false`](../../Swift/false.md), this property’s value is always [`false`](../../Swift/false.md).

This property supports key-value observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationscene)*