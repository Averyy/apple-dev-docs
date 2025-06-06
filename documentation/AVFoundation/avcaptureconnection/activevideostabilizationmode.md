# activeVideoStabilizationMode

**Framework**: Avfoundation  
**Kind**: property

The connection’s current stabilization mode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode { get }
```

#### Discussion

The property only applies to a video connection, and it explicitly indicates whether it’s using stabilization, which means the value is never [`AVCaptureVideoStabilizationMode.auto`](avcapturevideostabilizationmode/auto.md).

> **Note**:  Devices with a video stabilization feature may only support a subset of available source formats.

You can monitor this property to detect when the connection applies video stabilization to its video data with key-value observation. See [`NSKeyValueObserving`](https://developer.apple.com/documentation/ObjectiveC/nskeyvalueobserving) and [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift) for more information.

## See Also

- [var isVideoStabilizationSupported: Bool](avcaptureconnection/isvideostabilizationsupported.md)
  A Boolean value that indicates whether this connection supports video stabilization.
- [var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode](avcaptureconnection/preferredvideostabilizationmode.md)
  The stabilization mode that’s the most appropriate for a video connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/activevideostabilizationmode)*