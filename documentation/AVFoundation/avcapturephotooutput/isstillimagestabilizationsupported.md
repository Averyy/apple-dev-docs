# isStillImageStabilizationSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the capture output currently supports automatic stabilization for still image capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isStillImageStabilizationSupported: Bool { get }
```

#### Discussion

To capture a photo with image stabilization, set the [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md) property of your photo settings object. Automatic stabilization always includes digital image stabilization, and may also include optical lens stabilization, based on the current device. If a device does not support still image stabilization, set the [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md) property has no effect (that is, the resolved [`isStillImageStabilizationEnabled`](avcaptureresolvedphotosettings/isstillimagestabilizationenabled.md) setting will always be [`false`](https://developer.apple.com/documentation/swift/false)).

> **Note**:  This property’s value can change if the [`sessionPreset`](avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](avcapturedevice/activeformat.md) property of the underlying capture device changes.

This property supports key-value observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationsupported)*