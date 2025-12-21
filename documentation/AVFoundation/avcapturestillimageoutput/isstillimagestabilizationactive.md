# isStillImageStabilizationActive

**Framework**: AVFoundation  
**Kind**: property

Indicates whether still image stabilization is in use for the current capture.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isStillImageStabilizationActive: Bool { get }
```

#### Discussion

The property returns [`true`](https://developer.apple.com/documentation/Swift/true) if video stabilization is currently in use; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

This property supports key-value observing.

## See Also

- [var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool](avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable.md)
  A Boolean value that indicates whether still image stabilization should be automatically enabled.
- [var isStillImageStabilizationSupported: Bool](avcapturestillimageoutput/isstillimagestabilizationsupported.md)
  A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationactive)*