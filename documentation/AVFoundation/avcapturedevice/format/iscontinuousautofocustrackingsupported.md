# isContinuousAutoFocusTrackingSupported

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the device format supports continuous autofocus tracking.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isContinuousAutoFocusTrackingSupported: Bool { get }
```

#### Discussion

Continuous autofocus tracking allows the device to keep a subject in focus by monitoring it as it moves throughout the scene. The device’s [`isContinuousAutoFocusTrackingEnabled`](avcapturedevice/iscontinuousautofocustrackingenabled.md) property can only be set if this property returns `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscontinuousautofocustrackingsupported)*