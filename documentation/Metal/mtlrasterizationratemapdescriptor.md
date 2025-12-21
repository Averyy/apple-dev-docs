# MTLRasterizationRateMapDescriptor

**Framework**: Metal  
**Kind**: class

An object that you use to configure new rasterization rate maps.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLRasterizationRateMapDescriptor
```

#### Overview

To create a new rate map, first create an [`MTLRasterizationRateMapDescriptor`](mtlrasterizationratemapdescriptor.md) instance and set its property values. Then, create a new rasterization rate-map by calling an [`MTLDevice`](mtldevice.md) instance’s
[`makeRasterizationRateMap(descriptor:)`](mtldevice/makerasterizationratemap(descriptor:).md) method.

When creating a rate map, Metal copies into it property values from the descriptor. You can reuse a descrptor by modifying its property values, which doesn’t affect the other rate-map instances that already exist.

## Topics

### Creating rate map descriptors
- [convenience init(screenSize: MTLSize, label: String?)](mtlrasterizationratemapdescriptor/init(screensize:label:).md)
  A convenience initializer that creates a rate map descriptor with a given size and identifier.
- [convenience init(screenSize: MTLSize, layer: MTLRasterizationRateLayerDescriptor, label: String?)](mtlrasterizationratemapdescriptor/init(screensize:layer:label:).md)
  A convenience initializer that creates a rate map descriptor with a single rate layer.
- [convenience init(screenSize: MTLSize, layers: [MTLRasterizationRateLayerDescriptor], label: String?)](mtlrasterizationratemapdescriptor/init(screensize:layers:label:).md)
  A convenience initializer that creates a rate map descriptor with a set of layer descriptors.
### Identifying the rate map
- [var label: String?](mtlrasterizationratemapdescriptor/label.md)
  A string used to identify the rate map you create with the descriptor.
### Configuring the viewport size
- [var screenSize: MTLSize](mtlrasterizationratemapdescriptor/screensize.md)
  The size of the viewport coordinate system, in logical pixels.
### Configuring the rate map layers
- [var layerCount: Int](mtlrasterizationratemapdescriptor/layercount.md)
  The number of layers in the rate map.
- [func layer(at: Int) -> MTLRasterizationRateLayerDescriptor?](mtlrasterizationratemapdescriptor/layer(at:).md)
  Returns the layer description for a layer in the rate map.
- [func setLayer(MTLRasterizationRateLayerDescriptor?, at: Int)](mtlrasterizationratemapdescriptor/setlayer(_:at:).md)
  Sets a configuration for a layer rate map.
- [var layers: MTLRasterizationRateLayerArray](mtlrasterizationratemapdescriptor/layers.md)
  The rasterization rates for one or more layers in the rate map.
- [class MTLRasterizationRateLayerArray](mtlrasterizationratelayerarray.md)
  Descriptions for the rasterization rates to apply to the set of layers in a rate map.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md)
  Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md)
  Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md)
  Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md)
  Use the rate map data to scale the content to fill your destination texture.
- [protocol MTLRasterizationRateMap](mtlrasterizationratemap.md)
  A compiled read-only instance that determines how to apply variable rasterization rates when rendering.
- [typealias MTLCoordinate2D](mtlcoordinate2d.md)
  A coordinate in the viewport.
- [func MTLCoordinate2DMake(Float, Float) -> MTLCoordinate2D](mtlcoordinate2dmake(_:_:).md)
  Returns a new 2D point with the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor)*