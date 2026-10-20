# layer(at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Returns the layer description for a layer in the rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func layer(at layerIndex: Int) -> MTLRasterizationRateLayerDescriptor?
```

```objc
- (MTLRasterizationRateLayerDescriptor *) layerAtIndex:(NSUInteger) layerIndex;
```

#### Return Value

The [`MTLRasterizationRateLayerDescriptor`](../mtlrasterizationratelayerdescriptor.md) instance for the given index, or `nil` if you haven’t set an instance for this index.

#### Discussion

Calling this method is equivalent to using array subscript syntax.

## Parameters

- `layerIndex`: The entry to return.

## See Also

### Configuring the rate map layers
- [var layerCount: Int](./layercount.md)
  The number of layers in the rate map.
- [func setLayer(MTLRasterizationRateLayerDescriptor?, at: Int)](./setlayer%28_,at%29.md)
  Sets a configuration for a layer rate map.
- [var layers: MTLRasterizationRateLayerArray](./layers.md)
  The rasterization rates for one or more layers in the rate map.
- [class MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md)
  Descriptions for the rasterization rates to apply to the set of layers in a rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/layer(at:))*