# forceSDR

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A policy that forces conversion to standard dynamic range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static let forceSDR: AVAssetImageGenerator.DynamicRangePolicy
```

```c
extern AVAssetImageGeneratorDynamicRangePolicy const AVAssetImageGeneratorDynamicRangePolicyForceSDR;
```

## Discussion

This policy converts PQ or HLG transfer functions to 709, while maintaining color primaries and matrix.

## See Also

### Policies
- [static let matchSource: AVAssetImageGenerator.DynamicRangePolicy](./matchsource.md)
  A policy that preserves the color parameters of the source media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/forcesdr)*