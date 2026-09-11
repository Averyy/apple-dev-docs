# automaticallyEnablesLowLightVideoNoiseReduction

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the connection should automatically enable low light video noise reduction when the connection supports it.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var automaticallyEnablesLowLightVideoNoiseReduction: Bool { get set }
```

#### Discussion

On a connection where [`isLowLightVideoNoiseReductionSupported`](avcaptureconnection/islowlightvideonoisereductionsupported.md) is `true`, the system can enable low light video noise reduction to improve video quality at the cost of additional power. This property defaults to `true` for movie file output connections. When [`automaticallyEnablesLowLightVideoNoiseReduction`](avcaptureconnection/automaticallyenableslowlightvideonoisereduction.md) is `true`, the connection sets [`isLowLightVideoNoiseReductionEnabled`](avcaptureconnection/islowlightvideonoisereductionenabled.md) to `true` automatically when the session configuration is committed and the connection supports the feature. For `AVCaptureMultiCamSession` configurations with multiple movie file outputs, automatic enablement is suppressed because the feature can only be active on one output at a time; in that case, set this property to `false` and control [`isLowLightVideoNoiseReductionEnabled`](avcaptureconnection/islowlightvideonoisereductionenabled.md) directly on the desired connection. Enabling the feature on more than one movie file output connection increases the session’s `hardwareCost` and may result in an `AVCaptureSessionRuntimeErrorNotification`. Setting this property on a connection that does not support low light video noise reduction is permitted but has no effect. Clients can key-value observe [`isLowLightVideoNoiseReductionEnabled`](avcaptureconnection/islowlightvideonoisereductionenabled.md) to know when the connection has automatically changed the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyenableslowlightvideonoisereduction)*