# distance(from:)

**Framework**: Core Location  
**Kind**: method

Returns the distance (measured in meters) from the current object’s location to the specified location.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func distance(from location: CLLocation) -> CLLocationDistance
```

#### Return Value

The distance (in meters) between the two locations.

#### Discussion

This method measures the distance between the location in the current object and the value in the `location` parameter. The distance is calculated by tracing a line between the two points that follows the curvature of the Earth, and measuring the length of the resulting arc. The arc is a smooth curve that doesn’t take into account altitude changes between the two locations.

## Parameters

- `location`: The destination location.

## See Also

- [func getDistanceFrom(CLLocation) -> CLLocationDistance](cllocation/getdistancefrom(_:).md)
  Returns the distance (measured in meters) from the current object’s location to the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/distance(from:))*