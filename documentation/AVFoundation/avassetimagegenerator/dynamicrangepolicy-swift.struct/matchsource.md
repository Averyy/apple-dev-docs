# matchSource

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A policy that preserves the color parameters of the source media.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static let matchSource: AVAssetImageGenerator.DynamicRangePolicy
```

```c
extern AVAssetImageGeneratorDynamicRangePolicy const AVAssetImageGeneratorDynamicRangePolicyMatchSource;
```

## Discussion

By default, an image generator converts images to standard dynamic range. When working with HDR video, use this policy to preserve HDR color in the resulting images.

## See Also

### Policies
- [static let forceSDR: AVAssetImageGenerator.DynamicRangePolicy](./forcesdr.md)
  A policy that forces conversion to standard dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/matchsource)*