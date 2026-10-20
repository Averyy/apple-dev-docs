# setLayer(_:at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets a configuration for a layer rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setLayer(_ layer: MTLRasterizationRateLayerDescriptor?, at layerIndex: Int)
```

```objc
- (void) setLayer:(MTLRasterizationRateLayerDescriptor *) layer atIndex:(NSUInteger) layerIndex;
```

#### Discussion

Calling this method is equivalent to using array subscript syntax.

## Parameters

- `layer`: A description of a layer to add to the rate map descriptor. Use `nil` to remove the layer at that index.
- `layerIndex`: The index to put the new layer description in.

## See Also

### Configuring the rate map layers
- [var layerCount: Int](./layercount.md)
  The number of layers in the rate map.
- [func layer(at: Int) -> MTLRasterizationRateLayerDescriptor?](./layer%28at%29.md)
  Returns the layer description for a layer in the rate map.
- [var layers: MTLRasterizationRateLayerArray](./layers.md)
  The rasterization rates for one or more layers in the rate map.
- [class MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md)
  Descriptions for the rasterization rates to apply to the set of layers in a rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/setlayer(_:at:))*