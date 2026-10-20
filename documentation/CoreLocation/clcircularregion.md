# CLCircularRegion

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

A circular geographic region that a center point and radius deine.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CLCircularGeographicCondition`](./clcirculargeographiccondition.md) instead.

## Declaration

```swift
class CLCircularRegion
```

```objc
@interface CLCircularRegion : CLRegion
```

#### Overview

The [`CLCircularRegion`](./clcircularregion.md) class defines the location and boundaries for a circular geographic region. You can use instances of this class to define geofences for a specific location. The crossing of a geofence’s boundary causes the location manager to notify its delegate.

## Topics

### Creating a circular region
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](./clcircularregion/init%28center,radius,identifier%29.md)
  Creates and returns a region object defining a circular geographic area.
### Getting the circle’s center and radius
- [var center: CLLocationCoordinate2D](./clcircularregion/center.md)
  The center point of the geographic area.
- [var radius: CLLocationDistance](./clcircularregion/radius.md)
  The radius (measured in meters) that defines the geographic area’s outer boundary.
### Performing hit testing in the region
- [func contains(CLLocationCoordinate2D) -> Bool](./clcircularregion/contains%28_%29.md)
  Returns a Boolean value indicating whether the geographic area contains the specified coordinate.

## Relationships

### Inherits From
- [CLRegion](./clregion.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [class CLBeaconRegion](./clbeaconregion.md)
  A region for detecting the presence of iBeacon devices.
- [class CLBeaconIdentityConstraint](./clbeaconidentityconstraint.md)
  Identity characteristics that can match one or more beacons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcircularregion)*