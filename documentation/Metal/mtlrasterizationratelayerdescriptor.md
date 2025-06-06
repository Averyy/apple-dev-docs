# MTLRasterizationRateLayerDescriptor

**Framework**: Metal  
**Kind**: class

The minimum rasterization rates to apply to sections of a layer in the render target.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLRasterizationRateLayerDescriptor
```

#### Overview

Use a layer map to divide the logical viewport coordinate system into a 2D grid of equal-sized rectangles, and choose different rasterization rates for each cell.

Specify rasterization rates using floating-point numbers between `0.0` and `1.0`, inclusive. A rate of `1.0` represents the normal rasterization rate, where each logical unit is equal to a physical pixel; a rate of `0.5` means that two logical units equate to one physical pixel, and so on. A value of `0.0` means that the GPU renders at its lowest quality level. When you create the map, the device object chooses the nearest rasterization rate supported by the GPU that meets or exceeds the rate you specified.

In the layer map, you provide separate rasterization rates for the grid’s rows and columns. The horizontal rates specify a horizontal rasterization rate for each column, and the vertical rates specify a vertical rasterization rate for each row. Each cell calculates its physical size in pixels by using the logical size of cells in the map, the horizontal rate from the cell’s column, and the vertical rate from its row.

## Topics

### Creating a Layer Rasterization Rate Descriptor
- [init(sampleCount: MTLSize)](mtlrasterizationratelayerdescriptor/init(samplecount:).md)
  Initializes the layer map with an empty grid.
- [convenience init(horizontal: [Float], vertical: [Float])](mtlrasterizationratelayerdescriptor/init(horizontal:vertical:).md)
  Initializes a layer rate map with a set of horizontal and vertical rasterization rates.
### Inspecting the Layer Rate Function Parameters
- [var sampleCount: MTLSize](mtlrasterizationratelayerdescriptor/samplecount.md)
  The number of rows and columns in the layer map.
- [var maxSampleCount: MTLSize](mtlrasterizationratelayerdescriptor/maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](mtlrasterizationratelayerdescriptor/horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](mtlrasterizationratelayerdescriptor/vertical.md)
  The vertical rasterization rates for the layer map’s rows.
- [class MTLRasterizationRateSampleArray](mtlrasterizationratesamplearray.md)
  An array object that contains rasterization rates.

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

- [subscript(Int) -> MTLRasterizationRateLayerDescriptor?](mtlrasterizationratelayerarray/subscript(_:).md)
  Retrieves the sample value at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor)*