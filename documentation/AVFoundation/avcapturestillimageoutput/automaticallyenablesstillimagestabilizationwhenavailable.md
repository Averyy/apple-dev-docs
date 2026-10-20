# automaticallyEnablesStillImageStabilizationWhenAvailable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether still image stabilization should be automatically enabled.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

## Declaration

```swift
var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyEnablesStillImageStabilizationWhenAvailable;
```

#### Discussion

If [`isStillImageStabilizationSupported`](./isstillimagestabilizationsupported.md) returns [`true`](../../Swift/true.md), image stabilization may be applied to reduce blur commonly found in low light photos. When stabilization is enabled, still image captures incur additional latency.

The default value is [`true`](../../Swift/true.md) when supported by the input device; otherwise [`false`](../../Swift/false.md).

Setting this property throws an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)) if [`isStillImageStabilizationSupported`](./isstillimagestabilizationsupported.md) returns [`false`](../../Swift/false.md).

## See Also

### Getting and setting image stabilization settings
- [var isStillImageStabilizationActive: Bool](./isstillimagestabilizationactive.md)
  Indicates whether still image stabilization is in use for the current capture.
- [var isStillImageStabilizationSupported: Bool](./isstillimagestabilizationsupported.md)
  A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable)*