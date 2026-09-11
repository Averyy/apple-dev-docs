# isLowLightVideoNoiseReductionSupported

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the connection supports low light video noise reduction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var isLowLightVideoNoiseReductionSupported: Bool { get }
```

#### Discussion

This property returns `true` if the connection’s source device’s active format supports low light video noise reduction (see `AVCaptureDeviceFormat/isLowLightVideoNoiseReductionSupported`) and the connection’s output supports the feature. This value reflects the active configuration and can change as the active format, video stabilization mode, auto video frame rate, or maximum video frame rate changes. See [`automaticallyEnablesLowLightVideoNoiseReduction`](avcaptureconnection/automaticallyenableslowlightvideonoisereduction.md) for a detailed discussion. This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/islowlightvideonoisereductionsupported)*