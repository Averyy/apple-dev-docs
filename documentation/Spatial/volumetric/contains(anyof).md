# contains(anyOf:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether this volume contains any of the specified points.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func contains(anyOf points: [Point3D]) -> Bool
```

## Parameters

- `points`: The array of points that the function compares against.

## See Also

### Instance methods
- [func contains(Self) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the entity contains the specified volumetric entity.
- [func contains(point: Point3D) -> Bool](./contains%28point%29.md)
  Returns a Boolean value that indicates whether this volume contains the specified point.
- [func formIntersection(Self)](./formintersection%28_%29.md)
  Sets the primitive to the intersection of itself and the specified primitive.
- [func formUnion(Self)](./formunion%28_%29.md)
  Sets the primitive to the union of itself and the specified primitive.
- [func intersection(Self) -> Self?](./intersection%28_%29.md)
  Returns the intersection of two volumetric entities.
- [func union(Self) -> Self](./union%28_%29.md)
  Returns the smallest volumetric entity that contains the two source entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/volumetric/contains(anyof:))*