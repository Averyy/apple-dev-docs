# isStillImageStabilizationSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isStillImageStabilizationSupported: Bool { get }
```

#### Discussion

The  [`automaticallyEnablesStillImageStabilizationWhenAvailable`](avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable.md) property can only be set if this property returns [`true`](https://developer.apple.com/documentation/Swift/true).

The value may change as the session’s [`sessionPreset`](avcapturesession/sessionpreset.md) or the input device’s [`activeFormat`](avcapturedevice/activeformat.md) changes.

## See Also

- [var isStillImageStabilizationActive: Bool](avcapturestillimageoutput/isstillimagestabilizationactive.md)
  Indicates whether still image stabilization is in use for the current capture.
- [var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool](avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable.md)
  A Boolean value that indicates whether still image stabilization should be automatically enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationsupported)*