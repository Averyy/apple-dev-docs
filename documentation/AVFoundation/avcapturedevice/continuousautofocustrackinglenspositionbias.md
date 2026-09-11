# continuousAutoFocusTrackingLensPositionBias

**Framework**: AVFoundation  
**Kind**: property

Bias applied to the lens position during continuous autofocus tracking, normalized between -1 and 1.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var continuousAutoFocusTrackingLensPositionBias: Float { get set }
```

#### Discussion

While the device is actively tracking a subject to keep in focus, this property may be used to specify a bias applied to the lens position so that different portions of the subject are in focus. This property’s default value is 0 which aims to keep the median of the subject’s depth profile in focus. Values approaching -1 bias the lens position towards the closest portion of the depth profile while values approaching 1 bias the lens position towards the furthest portion of the profile. As the subject moves, the bias continues to apply to the subject’s new depth profile.

To apply bias updates, set the device’s focus mode to `AVCaptureFocusModeContinuousAutoFocus` after each change. The bias value has no effect otherwise. The value will only be automatically reset to 0 if cinematic video capture is enabled.

> **Note**: `NSInvalidArgumentException` if this property is set to a value other than 0 when the device’s [`isContinuousAutoFocusTrackingEnabled`](avcapturedevice/iscontinuousautofocustrackingenabled.md) is `false`.

> **Note**: `NSInvalidArgumentException` if this property is set to a value less than -1 or greater than 1.

> **Note**: `NSInvalidArgumentException` if this property is set to a non-zero value when the device is configured for cinematic video capture.

> **Note**: `NSGenericException` if the device is not locked for configuration using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/continuousautofocustrackinglenspositionbias)*