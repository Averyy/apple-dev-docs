# MTLRegionMake1D(_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Creates a 3D representation of a 1D region.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTLRegionMake1D(_ x: Int, _ width: Int) -> MTLRegion
```

```c
static MTLRegion MTLRegionMake1D(NSUInteger x, NSUInteger width);
```

#### Return Value

A region whose x and width values are as specified.  The y and z coordinates of the region’s origin are set to `0`, and the region’s height and depth are set to `1.`

## Parameters

- `x`: The x coordinate of the origin.
- `width`: The width of the volume.

## See Also

### Creating regions
- [init()](./mtlregion/init%28%29.md)
  Initializes a new region.
- [init(origin: MTLOrigin, size: MTLSize)](./mtlregion/init%28origin,size%29.md)
  Initializes a new region with the specified origin and size.
- [func MTLRegionMake2D(Int, Int, Int, Int) -> MTLRegion](./mtlregionmake2d%28_,_,_,_%29.md)
  Creates a 3D representation of a 2D region.
- [func MTLRegionMake3D(Int, Int, Int, Int, Int, Int) -> MTLRegion](./mtlregionmake3d%28_,_,_,_,_,_%29.md)
  Creates a 3D region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlregionmake1d(_:_:))*