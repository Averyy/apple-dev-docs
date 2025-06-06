# layerCount

**Framework**: Metal  
**Kind**: property

The number of layers in the rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var layerCount: Int { get }
```

#### Discussion

The value of this property is dynamically determined based on how many layers you’ve added to the descriptor. To add a new layer, call [`setLayer(_:at:)`](mtlrasterizationratemapdescriptor/setlayer(_:at:).md) or use the subscripting operator to assign a layer.

## See Also

- [func layer(at: Int) -> MTLRasterizationRateLayerDescriptor?](mtlrasterizationratemapdescriptor/layer(at:).md)
  Returns the layer description for a layer in the rate map.
- [func setLayer(MTLRasterizationRateLayerDescriptor?, at: Int)](mtlrasterizationratemapdescriptor/setlayer(_:at:).md)
  Sets a configuration for a layer rate map.
- [var layers: MTLRasterizationRateLayerArray](mtlrasterizationratemapdescriptor/layers.md)
  The rasterization rates for one or more layers in the rate map.
- [class MTLRasterizationRateLayerArray](mtlrasterizationratelayerarray.md)
  Descriptions for the rasterization rates to apply to the set of layers in a rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/layercount)*