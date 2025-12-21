# rasterizationRateMap

**Framework**: Metal  
**Kind**: property

The rasterization rate map to use when executing the render pass.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var rasterizationRateMap: (any MTLRasterizationRateMap)? { get set }
```

## Mentions

- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md)

#### Discussion

The default value is `nil`, which means that viewport coordinates are in the same coordinate system as the physical coordinates in the render target. Otherwise, Metal uses the rate map to convert between viewport coordinates and physical coordinates in the render target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/rasterizationratemap)*