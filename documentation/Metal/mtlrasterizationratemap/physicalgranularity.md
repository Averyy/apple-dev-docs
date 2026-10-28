# physicalGranularity

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The granularity, in physical pixels, at which the rasterization rate varies.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var physicalGranularity: MTLSize { get }
```

```objc
@property (readonly) MTLSize physicalGranularity;
```

## Discussion

If you’re using a rendering algorithm that uses binning or tiling to partition the rendered image, you may want to use the value of this property to determine your bin sizes.

The depth component of the returned [`MTLSize`](../mtlsize.md) structure is always `0`.

## See Also

### Inspecting geometric and rendering properties
- [var layerCount: Int](./layercount.md)
  The number of layers in the rate map.
- [var screenSize: MTLSize](./screensize.md)
  The logical size, in pixels, of the viewport coordinate system.
- [func physicalSize(layer: Int) -> MTLSize](./physicalsize%28layer%29.md)
  Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/physicalgranularity)*