# MTLRasterizationRateLayerArray

**Framework**: Metal  
**Kind**: class  
**Role**: Class

Descriptions for the rasterization rates to apply to the set of layers in a rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLRasterizationRateLayerArray
```

```objc
@interface MTLRasterizationRateLayerArray : NSObject
```

## Topics

### Accessing members of the array
- [subscript(Int) -> MTLRasterizationRateLayerDescriptor?](./mtlrasterizationratelayerarray/subscript%28_%29.md)
  Retrieves the sample value at the specified index.
- [class MTLRasterizationRateLayerDescriptor](./mtlrasterizationratelayerdescriptor.md)
  The minimum rasterization rates to apply to sections of a layer in the render target.
- [- setObject:atIndexedSubscript:](./mtlrasterizationratelayerarray/setobject_atindexedsubscript_.md)
  Stores a sample value at the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring the rate map layers
- [var layerCount: Int](./mtlrasterizationratemapdescriptor/layercount.md)
  The number of layers in the rate map.
- [func layer(at: Int) -> MTLRasterizationRateLayerDescriptor?](./mtlrasterizationratemapdescriptor/layer%28at%29.md)
  Returns the layer description for a layer in the rate map.
- [func setLayer(MTLRasterizationRateLayerDescriptor?, at: Int)](./mtlrasterizationratemapdescriptor/setlayer%28_,at%29.md)
  Sets a configuration for a layer rate map.
- [var layers: MTLRasterizationRateLayerArray](./mtlrasterizationratemapdescriptor/layers.md)
  The rasterization rates for one or more layers in the rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray)*