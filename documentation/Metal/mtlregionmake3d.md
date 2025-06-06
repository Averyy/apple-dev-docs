# MTLRegionMake3D(_:_:_:_:_:_:)

**Framework**: Metal  
**Kind**: func

Creates a 3D region.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func MTLRegionMake3D(_ x: Int, _ y: Int, _ z: Int, _ width: Int, _ height: Int, _ depth: Int) -> MTLRegion
```

#### Return Value

A 3D region with the specified values.

## Parameters

- `x`: The x coordinate of the origin.
- `y`: The y coordinate of the origin.
- `z`: The z coordinate of the origin.
- `width`: The width of the volume.
- `height`: The height of the volume.
- `depth`: The depth of the volume.

## See Also

- [init()](mtlregion/init.md)
  Initializes a new region.
- [init(origin: MTLOrigin, size: MTLSize)](mtlregion/init(origin:size:).md)
  Initializes a new region with the specified origin and size.
- [func MTLRegionMake1D(Int, Int) -> MTLRegion](mtlregionmake1d(_:_:).md)
  Creates a 3D representation of a 1D region.
- [func MTLRegionMake2D(Int, Int, Int, Int) -> MTLRegion](mtlregionmake2d(_:_:_:_:).md)
  Creates a 3D representation of a 2D region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlregionmake3d(_:_:_:_:_:_:))*