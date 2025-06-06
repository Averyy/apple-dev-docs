# CLCircularRegion

**Framework**: Core Location  
**Kind**: class

A circular geographic region that a center point and radius deine.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
class CLCircularRegion
```

#### Overview

The [`CLCircularRegion`](clcircularregion.md) class defines the location and boundaries for a circular geographic region. You can use instances of this class to define geofences for a specific location. The crossing of a geofence’s boundary causes the location manager to notify its delegate.

## Topics

### Creating a circular region
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](clcircularregion/init(center:radius:identifier:).md)
  Creates and returns a region object defining a circular geographic area.
### Getting the circle’s center and radius
- [var center: CLLocationCoordinate2D](clcircularregion/center.md)
  The center point of the geographic area.
- [var radius: CLLocationDistance](clcircularregion/radius.md)
  The radius (measured in meters) that defines the geographic area’s outer boundary.
### Performing hit testing in the region
- [func contains(CLLocationCoordinate2D) -> Bool](clcircularregion/contains(_:).md)
  Returns a Boolean value indicating whether the geographic area contains the specified coordinate.

## Relationships

### Inherits From
- [CLRegion](clregion.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CLBeaconRegion](clbeaconregion.md)
  A region for detecting the presence of iBeacon devices.
- [class CLBeaconIdentityConstraint](clbeaconidentityconstraint.md)
  Identity characteristics that can match one or more beacons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcircularregion)*