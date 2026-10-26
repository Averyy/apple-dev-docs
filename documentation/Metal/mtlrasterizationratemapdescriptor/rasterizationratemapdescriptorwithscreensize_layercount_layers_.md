# rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:

**Framework**: Metal  
**Kind**: method  
**Role**: Type Method

Creates a rate map descriptor with a set of layer descriptors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (MTLRasterizationRateMapDescriptor *) rasterizationRateMapDescriptorWithScreenSize:(MTLSize) screenSize layerCount:(NSUInteger) layerCount layers:(MTLRasterizationRateLayerDescriptor * const*) layers;
```

#### Return Value

A descriptor object whose [`screenSize`](./screensize.md) is set to the provided size and whose rate map layers are set to the array you provided.

## Parameters

- `screenSize`: The logical size, in pixels, of the viewport coordinate system.
- `layerCount`: The number of array elements in `layers`.
- `layers`: An array of rate layer descriptors for the rate map’s layers.

## See Also

### Creating rate map descriptors
- [+ rasterizationRateMapDescriptorWithScreenSize:](./rasterizationratemapdescriptorwithscreensize_.md)
  Creates a rate map descriptor with a given size and identifier.
- [+ rasterizationRateMapDescriptorWithScreenSize:layer:](./rasterizationratemapdescriptorwithscreensize_layer_.md)
  Creates a rate map descriptor with a single rate layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:layercount:layers:)*