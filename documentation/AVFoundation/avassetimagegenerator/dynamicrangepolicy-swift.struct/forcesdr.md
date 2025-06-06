# forceSDR

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

This policy converts PQ or HLG transfer functions to 709, while maintaining color primaries and matrix.

## See Also

- [static let matchSource: AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.struct/matchsource.md)
  A policy that preserves the color parameters of the source media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct/forcesdr)*