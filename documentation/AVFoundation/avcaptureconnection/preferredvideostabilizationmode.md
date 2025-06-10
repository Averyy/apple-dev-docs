# preferredVideoStabilizationMode

**Framework**: AVFoundation  
**Kind**: property

The stabilization mode that’s the most appropriate for a video connection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode { get set }
```

#### Discussion

The property only applies to a video connection, and defaults to [`AVCaptureVideoStabilizationMode.off`](avcapturevideostabilizationmode/off.md).

You can enable video stabilization by setting it to an available stabilization mode (other than [`AVCaptureVideoStabilizationMode.off`](avcapturevideostabilizationmode/off.md)). Video stabilization introduces additional latency into the video capture pipeline and may consume more system memory, depending on the stabilization mode and format. If a stabilization mode isn’t available, the connection sets its [`activeVideoStabilizationMode`](avcaptureconnection/activevideostabilizationmode.md) property to [`AVCaptureVideoStabilizationMode.off`](avcapturevideostabilizationmode/off.md). You can make the connection use an appropriate capture format and frame rate by setting the property to [`AVCaptureVideoStabilizationMode.auto`](avcapturevideostabilizationmode/auto.md).

> **Note**:  Devices with a video stabilization feature may only support a subset of available source formats.

Use key-value observing with the [`activeVideoStabilizationMode`](avcaptureconnection/activevideostabilizationmode.md) property to determine which stabilization mode is in use.

You can monitor the [`activeVideoStabilizationMode`](avcaptureconnection/activevideostabilizationmode.md) property to detect which stabilization mode the connection’s using. See [`NSKeyValueObserving`](https://developer.apple.com/documentation/ObjectiveC/nskeyvalueobserving) and [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift) for more information.

## See Also

- [var isVideoStabilizationSupported: Bool](avcaptureconnection/isvideostabilizationsupported.md)
  A Boolean value that indicates whether this connection supports video stabilization.
- [var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode](avcaptureconnection/activevideostabilizationmode.md)
  The connection’s current stabilization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/preferredvideostabilizationmode)*