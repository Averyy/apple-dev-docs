# displayVideoZoomFactorMultiplier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A video zoom factor multiplier to use when displaying zoom information in a user interface.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var displayVideoZoomFactorMultiplier: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat displayVideoZoomFactorMultiplier;
```

#### Discussion

Some system user interfaces, like the macOS Video Effects Menu, display a video zoom factor value in a way most appropriate for visual presentation, which might differ from the [`videoZoomFactor`](./videozoomfactor.md) property value.

Your app can key-value observe this property to update the display video zoom factor values in its user interface to stay consistent with Apple’s system UIs.

## See Also

### Inspecting zoom factors
- [var minAvailableVideoZoomFactor: CGFloat](./minavailablevideozoomfactor.md)
  The minimum zoom factor allowed in the current capture configuration.
- [var maxAvailableVideoZoomFactor: CGFloat](./maxavailablevideozoomfactor.md)
  The maximum zoom factor allowed in the current capture configuration.
- [var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber]](./virtualdeviceswitchovervideozoomfactors.md)
  An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [var dualCameraSwitchOverVideoZoomFactor: CGFloat](./dualcameraswitchovervideozoomfactor.md)
  The video zoom factor at which a dual camera device can automatically switch between cameras.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/displayvideozoomfactormultiplier)*