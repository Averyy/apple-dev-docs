# isVideoStabilizationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this connection supports video stabilization.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isVideoStabilizationSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoStabilizationSupported) BOOL supportsVideoStabilization;
```

## Discussion

The connection only supports video stabilization for video connection types, but may not be available for all resolutions.

## See Also

### Stabilizing video
- [var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode](./activevideostabilizationmode.md)
  The connection’s current stabilization mode.
- [var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode](./preferredvideostabilizationmode.md)
  The stabilization mode that’s the most appropriate for a video connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideostabilizationsupported)*