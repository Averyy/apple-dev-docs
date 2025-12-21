# MTLSize

**Framework**: Metal  
**Kind**: struct

A type that represents one, two, or three dimensions of a type instance, such as an array or texture.

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

- [Converting between pixel regions and sparse tile regions](converting-between-pixel-regions-and-sparse-tile-regions.md)
- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md)
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md)

#### Overview

Metal has many types that represent arrays of discrete elements, such as:

- A texture, which has an array of pixel elements
- A thread grid, which has an array of computational threads

Types and methods that work with these array-like types frequently have an [`MTLSize`](mtlsize.md) property or parameter that refers to the extents of a specific instance of the type, or a region within the instance.

> ❗ **Important**: Treat each size instance as a measure of something in 3D, even if it represents something with only one or two dimensions, by assigning `1` to the irrelevant dimensions.

The following are some examples for setting a size for an instance that has less than three dimentions:

- For a 2D texture that has a height and width of `5`, set a size’s [`depth`](mtlsize/depth.md) property to `1` so that it represents `[5, 5, 1]`.
- For a 1D array with length `42`, set a size’s [`height`](mtlsize/height.md), [`depth`](mtlsize/depth.md) properties to `1`, so that it represents `[42, 1, 1]`.

## Topics

### Creating a size instance
- [init()](mtlsize/init.md)
  Creates a default size instance by setting the initial values for its width, height, and depth properties to zero.
- [init(width: Int, height: Int, depth: Int)](mtlsize/init(width:height:depth:).md)
  Creates a size instance with values for its width, height, and depth properties.
- [func MTLSizeMake(Int, Int, Int) -> MTLSize](mtlsizemake(_:_:_:).md)
  Creates a size instance with values for its width, height, and depth properties.
### Accessing a size’s dimensions
- [var width: Int](mtlsize/width.md)
  A value for the x-axis dimension.
- [var height: Int](mtlsize/height.md)
  A value for the y-axis dimension.
- [var depth: Int](mtlsize/depth.md)
  A value for the z-axis dimension.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIndirectComputeCommand](mtlindirectcomputecommand.md)
  A compute command in an indirect command buffer.
- [struct MTLRegion](mtlregion.md)
  The bounds for a subset of an instance’s elements.
- [struct MTLOrigin](mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsize)*