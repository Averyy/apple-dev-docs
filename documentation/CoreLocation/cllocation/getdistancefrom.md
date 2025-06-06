# getDistanceFrom(_:)

**Framework**: Core Location  
**Kind**: method

Returns the distance (measured in meters) from the current object’s location to the specified location.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance
```

#### Return Value

The distance (in meters) between the two locations.

#### Discussion

This method measures the distance between the location in the current object and the value in the `location` parameter. The distance is calculated by tracing a line between the two points that follows the curvature of the Earth, and measuring the length of the resulting arc. The arc is a smooth curve that does not take into account altitude changes between the two locations.

## Parameters

- `location`: The other location.

## See Also

- [func distance(from: CLLocation) -> CLLocationDistance](cllocation/distance(from:).md)
  Returns the distance (measured in meters) from the current object’s location to the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/getdistancefrom(_:))*