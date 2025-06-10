# extendedDynamicRangeHeadroom

**Framework**: RealityKit  
**Kind**: property

The amount of headroom available for extended dynamic range content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
var extendedDynamicRangeHeadroom: Float { get set }
```

#### Discussion

When EDR output is enabled using [`extendedDynamicRangeOutput`](realityrenderer/extendeddynamicrangeoutput.md), standard dynamic range values output by this [`RealityRenderer`](realityrenderer.md) will be scaled such that there’s some  to display extended range values.

This value is in the range `[1.0-16.0]`. The default value is `2.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/extendeddynamicrangeheadroom)*