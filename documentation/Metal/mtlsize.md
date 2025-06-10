# MTLSize

**Framework**: Metal  
**Kind**: struct

The dimensions of an object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLSize
```

## Mentions

- [Converting Between Pixel Regions and Sparse Tile Regions](converting-between-pixel-regions-and-sparse-tile-regions.md)
- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)
- [Creating a Rasterization Rate Map](creating-a-rasterization-rate-map.md)

#### Overview

Metal has many object types that represent arrays of discrete elements. For example, a texture has an array of pixel elements, and a thread grid has an array of computational threads. Use [`MTLSize`](mtlsize.md) instances to measure the extents of these objects or extents of regions within these objects.

Conceptually, when using a [`MTLSize`](mtlsize.md) instance to measure an object, treat the object as a 3D array of elements, even if it has fewer dimensions. Set the length of any unused dimensions to `1`. For example, a `5x5` 2D texture is a `5x5x1` texture in 3D.

## Topics

### Creating Sizes
- [init()](mtlsize/init.md)
  Initializes a box size.
- [init(width: Int, height: Int, depth: Int)](mtlsize/init(width:height:depth:).md)
  Initializes a size for an object with the specified dimensions.
- [func MTLSizeMake(Int, Int, Int) -> MTLSize](mtlsizemake(_:_:_:).md)
  Creates a size for an object using the specified dimensions.
### Getting and Setting Dimensions
- [var width: Int](mtlsize/width.md)
  The number of elements in the x dimension.
- [var height: Int](mtlsize/height.md)
  The number of elements in the y dimension.
- [var depth: Int](mtlsize/depth.md)
  The number of elements in the z dimension.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIndirectComputeCommand](mtlindirectcomputecommand.md)
  A compute command in an indirect command buffer.
- [struct MTLRegion](mtlregion.md)
  The bounds for a subset of an object’s elements.
- [struct MTLOrigin](mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsize)*