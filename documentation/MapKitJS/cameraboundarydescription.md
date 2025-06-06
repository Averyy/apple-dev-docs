# CameraBoundaryDescription

**Framework**: MapKit JS  
**Kind**: struct

An object literal containing at least one property defining an area on the map.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
dictionary CameraBoundaryDescription {
	mapkit.MapRect mapRect;
	mapkit.CoordinateRegion region;
};
```

#### Overview

The `CameraBoundaryDescription` can contain the `mapRect` or `region` properties, or both. Both properties describe a rectangular area on the map.

## Topics

### Defining a Camera Boundary
- [mapRect](cameraboundarydescription/maprect.md)
  A rectangular area on a two-dimensional map projection.
- [region](cameraboundarydescription/region.md)
  A rectangular area on a map, defined by coordinates of the rectangle’s northeast and southwest corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/cameraboundarydescription)*