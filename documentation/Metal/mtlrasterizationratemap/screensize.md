# screenSize

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The logical size, in pixels, of the viewport coordinate system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var screenSize: MTLSize { get }
```

## Mentions

- [Rendering with a Rasterization Rate Map](rendering-with-a-rasterization-rate-map.md)

## See Also

- [var layerCount: Int](mtlrasterizationratemap/layercount.md)
  The number of layers in the rate map.
- [func physicalSize(layer: Int) -> MTLSize](mtlrasterizationratemap/physicalsize(layer:).md)
  Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.
- [var physicalGranularity: MTLSize](mtlrasterizationratemap/physicalgranularity.md)
  The granularity, in physical pixels, at which the rasterization rate varies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/screensize)*