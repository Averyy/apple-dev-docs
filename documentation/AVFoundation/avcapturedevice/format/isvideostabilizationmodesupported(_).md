# isVideoStabilizationModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates whether the format supports a given video stabilization mode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func isVideoStabilizationModeSupported(_ videoStabilizationMode: AVCaptureVideoStabilizationMode) -> Bool
```

```objc
- (BOOL) isVideoStabilizationModeSupported:(AVCaptureVideoStabilizationMode) videoStabilizationMode;
```

## Return Value

[`true`](../../../Swift/true.md) if video stabilization is supported; otherwise, [`false`](../../../Swift/false.md).

## Parameters

- `videoStabilizationMode`: The stabilization mode to test.

## See Also

### Determining video stabilization support
- [enum AVCaptureVideoStabilizationMode](../../avcapturevideostabilizationmode.md)
  An enumeration of video stabilization modes that capture devices and formats support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideostabilizationmodesupported(_:))*