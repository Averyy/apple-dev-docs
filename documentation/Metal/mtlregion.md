# MTLRegion

**Framework**: Metal  
**Kind**: struct

The bounds for a subset of an instance’s elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLRegion
```

## Mentions

- [Converting between pixel regions and sparse tile regions](converting-between-pixel-regions-and-sparse-tile-regions.md)

#### Overview

Metal has many instance types that represent arrays of discrete elements. For example, a texture has an array of pixel elements, and a thread grid has an array of computational threads. Use [`MTLRegion`](mtlregion.md) instances to describe subsets of these instances.

The origin is the front upper-left corner of the region, and its extents go towards the back lower-right corner. Conceptually, when using an [`MTLRegion`](mtlregion.md) instance to describe a subset of an instance, treat the instance as a 3D array of elements, even if it has fewer dimensions. For a 2D instance, set the z coordinate of the origin to `0` and the depth to `1`. For a 1D instance, set the y and z coordinates of the origin to `0` and the height and depth to `1`.

## Topics

### Creating regions
- [init()](mtlregion/init.md)
  Initializes a new region.
- [init(origin: MTLOrigin, size: MTLSize)](mtlregion/init(origin:size:).md)
  Initializes a new region with the specified origin and size.
- [func MTLRegionMake1D(Int, Int) -> MTLRegion](mtlregionmake1d(_:_:).md)
  Creates a 3D representation of a 1D region.
- [func MTLRegionMake2D(Int, Int, Int, Int) -> MTLRegion](mtlregionmake2d(_:_:_:_:).md)
  Creates a 3D representation of a 2D region.
- [func MTLRegionMake3D(Int, Int, Int, Int, Int, Int) -> MTLRegion](mtlregionmake3d(_:_:_:_:_:_:).md)
  Creates a 3D region.
### Getting and setting region information
- [var origin: MTLOrigin](mtlregion/origin.md)
  The coordinates of the front upper-left corner of the region.
- [var size: MTLSize](mtlregion/size.md)
  The dimensions of the region.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIndirectComputeCommand](mtlindirectcomputecommand.md)
  A compute command in an indirect command buffer.
- [struct MTLSize](mtlsize.md)
  A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [struct MTLOrigin](mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlregion)*