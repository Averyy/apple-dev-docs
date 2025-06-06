# init(origin:size:)

**Framework**: Metal  
**Kind**: init

Initializes a new region with the specified origin and size.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(origin: MTLOrigin, size: MTLSize)
```

## Parameters

- `origin`: The origin of the region.
- `size`: The size of the region.

## See Also

- [init()](mtlregion/init.md)
  Initializes a new region.
- [func MTLRegionMake1D(Int, Int) -> MTLRegion](mtlregionmake1d(_:_:).md)
  Creates a 3D representation of a 1D region.
- [func MTLRegionMake2D(Int, Int, Int, Int) -> MTLRegion](mtlregionmake2d(_:_:_:_:).md)
  Creates a 3D representation of a 2D region.
- [func MTLRegionMake3D(Int, Int, Int, Int, Int, Int) -> MTLRegion](mtlregionmake3d(_:_:_:_:_:_:).md)
  Creates a 3D region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlregion/init(origin:size:))*