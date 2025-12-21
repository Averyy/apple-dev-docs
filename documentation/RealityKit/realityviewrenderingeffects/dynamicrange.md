# dynamicRange

**Framework**: RealityKit  
**Kind**: property

Enables or disables high dynamic range rendering for virtual content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
var dynamicRange: RealityViewDynamicRange
```

#### Discussion

RealityKit applies a high dynamic range effect, along with tone mapping, as a post-processing step in the GPU during the render. This effect is computationally inexpensive, but you can add the [`disableHDR`](arview/renderoptions-swift.struct/disablehdr.md) option to the view’s [`renderOptions`](arview/renderoptions-swift.property.md) set to turn the effect off, if needed.

When deciding whether to use any effect, be sure to consider your app’s CPU and GPU utilization, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

> ❗ **Important**: This rendering effect is unavailable on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewrenderingeffects/dynamicrange)*