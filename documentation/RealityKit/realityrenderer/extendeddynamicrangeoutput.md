# extendedDynamicRangeOutput

**Framework**: RealityKit  
**Kind**: property

Specify whether the target Metal layer has been configured for EDR output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
var extendedDynamicRangeOutput: Bool { get set }
```

#### Discussion

If the Metal layer that this [`RealityRenderer`](realityrenderer.md) will be rendering into has been configured to output extended dynamic range content (i.e. the property `QuartzCore/CAMetalLayer/wantsExtendedDynamicRangeContent` on the target `QuartzCore/CAMetalLayer` has been set to `true` and a pixel format that supports EDR content has been set), this property should be set to `true` so that [`RealityRenderer`](realityrenderer.md) adjusts its tone mapping accordingly.

To control the amount of headroom available for extended dynamic range content, see [`extendedDynamicRangeHeadroom`](realityrenderer/extendeddynamicrangeheadroom.md).

The default value is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/extendeddynamicrangeoutput)*