# CLRegion

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

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

```objc
@interface CLRegion : NSObject
```

#### Overview

This is an abstract base class. Instantiate one of the provided subclasses that define specific types of regions. After you create a region, register it with a [`CLLocationManager`](./cllocationmanager.md) object with the [`startMonitoring(for:)`](./cllocationmanager/startmonitoring%28for%29.md) method. The location manager generates appropriate events whenever the user crosses the boundaries of the region.

## Topics

### Getting the region identifier
- [var identifier: String](./clregion/identifier.md)
  The identifier for the region object.
### Specifying the notification conditions
- [var notifyOnEntry: Bool](./clregion/notifyonentry.md)
  A Boolean indicating that notifications are generated upon entry into the region.
- [var notifyOnExit: Bool](./clregion/notifyonexit.md)
  A Boolean indicating that notifications are generated upon exit from the region.
### Deprecated
- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](./clregion/init%28circularregionwithcenter,radius,identifier%29.md)
  Initializes and returns a region object defining a circular area.
- [func contains(CLLocationCoordinate2D) -> Bool](./clregion/contains%28_%29.md)
  Returns a Boolean value indicating whether the region contains the specified coordinate.
- [var center: CLLocationCoordinate2D](./clregion/center.md)
  The center point of the region.
- [var radius: CLLocationDistance](./clregion/radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.
### Initializers
- [init?(coder: NSCoder)](./clregion/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CLBeaconRegion](./clbeaconregion.md)
- [CLCircularRegion](./clcircularregion.md)
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

### Region monitoring
- [Monitoring the user’s proximity to geographic regions](./monitoring-the-user-s-proximity-to-geographic-regions.md)
  Use condition monitoring to determine when the user enters or leaves a geographic region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion)*