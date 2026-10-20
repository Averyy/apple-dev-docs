# getDistanceFrom(_:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Returns the distance (measured in meters) from the current object’s location to the specified location.

**Availability**:
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use the [`distance(from:)`](./distance%28from%29.md) method instead.

## Declaration

```swift
func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance
```

```objc
- (CLLocationDistance) getDistanceFrom:(const CLLocation *) location;
```

#### Return Value

The distance (in meters) between the two locations.

#### Discussion

This method measures the distance between the location in the current object and the value in the `location` parameter. The distance is calculated by tracing a line between the two points that follows the curvature of the Earth, and measuring the length of the resulting arc. The arc is a smooth curve that does not take into account altitude changes between the two locations.

## Parameters

- `location`: The other location.

## See Also

### Measuring the distance between coordinates
- [func distance(from: CLLocation) -> CLLocationDistance](./distance%28from%29.md)
  Returns the distance (measured in meters) from the current object’s location to the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/getdistancefrom(_:))*