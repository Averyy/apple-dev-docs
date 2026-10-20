# physicalSize(layer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func physicalSize(layer layerIndex: Int) -> MTLSize
```

## Mentions

- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md)

#### Return Value

The dimensions, in pixels, of the area in the render target affected by the rasterization rate map.

#### Discussion

Your render targets should be at least as large as the physical size returned by this method. Each layer may have different rasterization rates and therefore different physical size requirements.

## Parameters

- `layerIndex`: The index of the layer.

## See Also

- [var layerCount: Int](mtlrasterizationratemap/layercount.md)
  The number of layers in the rate map.
- [var screenSize: MTLSize](mtlrasterizationratemap/screensize.md)
  The logical size, in pixels, of the viewport coordinate system.
- [var physicalGranularity: MTLSize](mtlrasterizationratemap/physicalgranularity.md)
  The granularity, in physical pixels, at which the rasterization rate varies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/physicalsize(layer:))*