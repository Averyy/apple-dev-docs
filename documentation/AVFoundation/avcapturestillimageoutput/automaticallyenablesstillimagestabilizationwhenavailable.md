# automaticallyEnablesStillImageStabilizationWhenAvailable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether still image stabilization should be automatically enabled.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool { get set }
```

#### Discussion

If [`isStillImageStabilizationSupported`](avcapturestillimageoutput/isstillimagestabilizationsupported.md) returns [`true`](https://developer.apple.com/documentation/swift/true), image stabilization may be applied to reduce blur commonly found in low light photos. When stabilization is enabled, still image captures incur additional latency.

The default value is [`true`](https://developer.apple.com/documentation/swift/true) when supported by the input device; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

Setting this property throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception)) if [`isStillImageStabilizationSupported`](avcapturestillimageoutput/isstillimagestabilizationsupported.md) returns [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isStillImageStabilizationActive: Bool](avcapturestillimageoutput/isstillimagestabilizationactive.md)
  Indicates whether still image stabilization is in use for the current capture.
- [var isStillImageStabilizationSupported: Bool](avcapturestillimageoutput/isstillimagestabilizationsupported.md)
  A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable)*