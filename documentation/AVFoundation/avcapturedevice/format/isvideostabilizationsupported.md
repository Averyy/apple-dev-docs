# isVideoStabilizationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format supports video stabilization.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use isVideoStabilizationModeSupported: instead.

## Declaration

```swift
var isVideoStabilizationSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoStabilizationSupported) BOOL videoStabilizationSupported;
```

#### Discussion

If the format supports video stabilization, you can enable it on an [`AVCaptureConnection`](../../avcaptureconnection.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideostabilizationsupported)*