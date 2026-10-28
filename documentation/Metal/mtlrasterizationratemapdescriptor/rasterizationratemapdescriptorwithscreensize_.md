# rasterizationRateMapDescriptorWithScreenSize:

**Framework**: Metal  
**Kind**: method  
**Role**: Type Method

Creates a rate map descriptor with a given size and identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (MTLRasterizationRateMapDescriptor *) rasterizationRateMapDescriptorWithScreenSize:(MTLSize) screenSize;
```

## Return Value

A descriptor object whose [`screenSize`](./screensize.md) is set to the provided size. You need to add at least one layer rate map to the descriptor.

## Parameters

- `screenSize`: The logical size, in pixels, of the viewport coordinate system.

## See Also

### Creating rate map descriptors
- [+ rasterizationRateMapDescriptorWithScreenSize:layer:](./rasterizationratemapdescriptorwithscreensize_layer_.md)
  Creates a rate map descriptor with a single rate layer.
- [+ rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:](./rasterizationratemapdescriptorwithscreensize_layercount_layers_.md)
  Creates a rate map descriptor with a set of layer descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:)*