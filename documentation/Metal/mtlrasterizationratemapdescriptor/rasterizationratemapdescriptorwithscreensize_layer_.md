# rasterizationRateMapDescriptorWithScreenSize:layer:

**Framework**: Metal  
**Kind**: method  
**Role**: Type Method

Creates a rate map descriptor with a single rate layer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (MTLRasterizationRateMapDescriptor *) rasterizationRateMapDescriptorWithScreenSize:(MTLSize) screenSize layer:(MTLRasterizationRateLayerDescriptor *) layer;
```

#### Return Value

A descriptor object whose [`screenSize`](./screensize.md) is set to the provided size. Layer 0 in the rate map is set to the provided layer descriptor.

## Parameters

- `screenSize`: The logical size, in pixels, of the viewport coordinate system.
- `layer`: A descriptor for the rate layer to create.

## See Also

### Creating rate map descriptors
- [+ rasterizationRateMapDescriptorWithScreenSize:](./rasterizationratemapdescriptorwithscreensize_.md)
  Creates a rate map descriptor with a given size and identifier.
- [+ rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:](./rasterizationratemapdescriptorwithscreensize_layercount_layers_.md)
  Creates a rate map descriptor with a set of layer descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:layer:)*