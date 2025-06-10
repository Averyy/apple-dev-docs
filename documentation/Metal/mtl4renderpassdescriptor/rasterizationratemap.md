# rasterizationRateMap

**Framework**: Metal  
**Kind**: property

Assigns an optional variable rasterization rate map that Metal uses in the render pass.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var rasterizationRateMap: (any MTLRasterizationRateMap)? { get set }
```

#### Discussion

Enabling variable rasterization rate allows Metal to decrease the rasterization rate, typically in unimportant regions of color attachments, to accelerate processing.

When set to `nil`, the default, Metal doesn’t use variable rasterization rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/rasterizationratemap)*