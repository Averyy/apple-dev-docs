# CLRegion

**Framework**: Core Location  
**Kind**: class

A base class representing an area that can be monitored.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
class CLRegion
```

#### Overview

This is an abstract base class. Instantiate one of the provided subclasses that define specific types of regions. After you create a region, register it with a [`CLLocationManager`](cllocationmanager.md) object with the [`startMonitoring(for:)`](cllocationmanager/startmonitoring(for:).md) method. The location manager generates appropriate events whenever the user crosses the boundaries of the region.

## Topics

### Getting the region identifier
- [var identifier: String](clregion/identifier.md)
  The identifier for the region object.
### Specifying the notification conditions
- [var notifyOnEntry: Bool](clregion/notifyonentry.md)
  A Boolean indicating that notifications are generated upon entry into the region.
- [var notifyOnExit: Bool](clregion/notifyonexit.md)
  A Boolean indicating that notifications are generated upon exit from the region.
### Deprecated
- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](clregion/init(circularregionwithcenter:radius:identifier:).md)
  Initializes and returns a region object defining a circular area.
- [func contains(CLLocationCoordinate2D) -> Bool](clregion/contains(_:).md)
  Returns a Boolean value indicating whether the region contains the specified coordinate.
- [var center: CLLocationCoordinate2D](clregion/center.md)
  The center point of the region.
- [var radius: CLLocationDistance](clregion/radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CLBeaconRegion](clbeaconregion.md)
- [CLCircularRegion](clcircularregion.md)
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

- [Monitoring the user’s proximity to geographic regions](monitoring-the-user-s-proximity-to-geographic-regions.md)
  Use condition monitoring to determine when the user enters or leaves a geographic region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion)*