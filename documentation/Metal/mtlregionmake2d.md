# MTLRegionMake2D(_:_:_:_:)

**Framework**: Metal  
**Kind**: func

Creates a 3D representation of a 2D region.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func MTLRegionMake2D(_ x: Int, _ y: Int, _ width: Int, _ height: Int) -> MTLRegion
```

#### Return Value

A region whose x, y, width, and height values are as specified. The z coordinate of the region’s origin is set to `0`, and the region’s depth is set to `1`.

## Parameters

- `x`: The x coordinate of the origin.
- `y`: The y coordinate of the origin.
- `width`: The width of the volume.
- `height`: The height of the volume.

## See Also

- [init()](mtlregion/init.md)
  Initializes a new region.
- [init(origin: MTLOrigin, size: MTLSize)](mtlregion/init(origin:size:).md)
  Initializes a new region with the specified origin and size.
- [func MTLRegionMake1D(Int, Int) -> MTLRegion](mtlregionmake1d(_:_:).md)
  Creates a 3D representation of a 1D region.
- [func MTLRegionMake3D(Int, Int, Int, Int, Int, Int) -> MTLRegion](mtlregionmake3d(_:_:_:_:_:_:).md)
  Creates a 3D region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlregionmake2d(_:_:_:_:))*