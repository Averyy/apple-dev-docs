# isStillImageStabilizationActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether still image stabilization is in use for the current capture.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

## Declaration

```swift
var isStillImageStabilizationActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isStillImageStabilizationActive) BOOL stillImageStabilizationActive;
```

## Discussion

The property returns [`true`](../../Swift/true.md) if video stabilization is currently in use; otherwise [`false`](../../Swift/false.md).

This property supports key-value observing.

## See Also

### Getting and setting image stabilization settings
- [var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool](./automaticallyenablesstillimagestabilizationwhenavailable.md)
  A Boolean value that indicates whether still image stabilization should be automatically enabled.
- [var isStillImageStabilizationSupported: Bool](./isstillimagestabilizationsupported.md)
  A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationactive)*