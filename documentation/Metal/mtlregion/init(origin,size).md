# init(origin:size:)

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Initializes a new region with the specified origin and size.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
init(origin: MTLOrigin, size: MTLSize)
```

## Parameters

- `origin`: The origin of the region.
- `size`: The size of the region.

## See Also

### Creating regions
- [init()](./init%28%29.md)
  Initializes a new region.
- [func MTLRegionMake1D(Int, Int) -> MTLRegion](../mtlregionmake1d%28_,_%29.md)
  Creates a 3D representation of a 1D region.
- [func MTLRegionMake2D(Int, Int, Int, Int) -> MTLRegion](../mtlregionmake2d%28_,_,_,_%29.md)
  Creates a 3D representation of a 2D region.
- [func MTLRegionMake3D(Int, Int, Int, Int, Int, Int) -> MTLRegion](../mtlregionmake3d%28_,_,_,_,_,_%29.md)
  Creates a 3D region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlregion/init(origin:size:))*