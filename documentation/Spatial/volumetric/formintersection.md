# formIntersection(_:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Sets the primitive to the intersection of itself and the specified primitive.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

## Parameters

- `other`: The volumetric entity that the function compares against.

## See Also

- [func contains(Self) -> Bool](volumetric/contains(_:).md)
  Returns a Boolean value that indicates whether the entity contains the specified volumetric entity.
- [func contains(point: Point3D) -> Bool](volumetric/contains(point:).md)
  Returns a Boolean value that indicates whether this volume contains the specified point.
- [func contains(anyOf: [Point3D]) -> Bool](volumetric/contains(anyof:).md)
  Returns a Boolean value that indicates whether this volume contains any of the specified points.
- [func formUnion(Self)](volumetric/formunion(_:).md)
  Sets the primitive to the union of itself and the specified primitive.
- [func intersection(Self) -> Self?](volumetric/intersection(_:).md)
  Returns the intersection of two volumetric entities.
- [func union(Self) -> Self](volumetric/union(_:).md)
  Returns the smallest volumetric entity that contains the two source entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/volumetric/formintersection(_:))*