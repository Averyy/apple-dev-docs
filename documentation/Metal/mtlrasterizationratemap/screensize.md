# screenSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) MTLSize screenSize;
```

## Mentions

- [Rendering with a rasterization rate map](../rendering-with-a-rasterization-rate-map.md)

## See Also

### Inspecting geometric and rendering properties
- [var layerCount: Int](./layercount.md)
  The number of layers in the rate map.
- [func physicalSize(layer: Int) -> MTLSize](./physicalsize%28layer%29.md)
  Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.
- [var physicalGranularity: MTLSize](./physicalgranularity.md)
  The granularity, in physical pixels, at which the rasterization rate varies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/screensize)*