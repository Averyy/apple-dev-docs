# MTLRasterizationRateLayerArray

**Framework**: Metal  
**Kind**: class

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

## Topics

### Accessing members of the array
- [subscript(Int) -> MTLRasterizationRateLayerDescriptor?](mtlrasterizationratelayerarray/subscript(_:).md)
  Retrieves the sample value at the specified index.
- [class MTLRasterizationRateLayerDescriptor](mtlrasterizationratelayerdescriptor.md)
  The minimum rasterization rates to apply to sections of a layer in the render target.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var layerCount: Int](mtlrasterizationratemapdescriptor/layercount.md)
  The number of layers in the rate map.
- [func layer(at: Int) -> MTLRasterizationRateLayerDescriptor?](mtlrasterizationratemapdescriptor/layer(at:).md)
  Returns the layer description for a layer in the rate map.
- [func setLayer(MTLRasterizationRateLayerDescriptor?, at: Int)](mtlrasterizationratemapdescriptor/setlayer(_:at:).md)
  Sets a configuration for a layer rate map.
- [var layers: MTLRasterizationRateLayerArray](mtlrasterizationratemapdescriptor/layers.md)
  The rasterization rates for one or more layers in the rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray)*