# rasterizationRateMap

**Framework**: Metal  
**Kind**: property

Assigns an optional variable rasterization rate map that Metal uses in the render pass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var rasterizationRateMap: (any MTLRasterizationRateMap)? { get set }
```

#### Discussion

Enabling variable rasterization rate allows Metal to decrease the rasterization rate, typically in unimportant regions of color attachments, to accelerate processing.

When set to `nil`, the default, Metal doesn’t use variable rasterization rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/rasterizationratemap)*