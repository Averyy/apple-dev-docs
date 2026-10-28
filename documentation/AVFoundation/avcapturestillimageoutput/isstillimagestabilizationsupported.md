# isStillImageStabilizationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

## Declaration

```swift
var isStillImageStabilizationSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isStillImageStabilizationSupported) BOOL stillImageStabilizationSupported;
```

## Discussion

The  [`automaticallyEnablesStillImageStabilizationWhenAvailable`](./automaticallyenablesstillimagestabilizationwhenavailable.md) property can only be set if this property returns [`true`](../../Swift/true.md).

The value may change as the session’s [`sessionPreset`](../avcapturesession/sessionpreset.md) or the input device’s [`activeFormat`](../avcapturedevice/activeformat.md) changes.

## See Also

### Getting and setting image stabilization settings
- [var isStillImageStabilizationActive: Bool](./isstillimagestabilizationactive.md)
  Indicates whether still image stabilization is in use for the current capture.
- [var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool](./automaticallyenablesstillimagestabilizationwhenavailable.md)
  A Boolean value that indicates whether still image stabilization should be automatically enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationsupported)*