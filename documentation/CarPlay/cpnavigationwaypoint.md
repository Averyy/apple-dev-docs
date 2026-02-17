# CPNavigationWaypoint

**Framework**: CarPlay  
**Kind**: class

CPNavigationWaypoint represents a point of interest along a route that provides location-based information and guidance.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
class CPNavigationWaypoint
```

## Topics

### Initializers
- [convenience init(centerPoint: CPLocationCoordinate3D, locationThreshold: Measurement<UnitLength>?, name: String?, address: String?, entryPoints: [CPLocationCoordinate3D], timeZone: TimeZone?)](cpnavigationwaypoint/init(centerpoint:locationthreshold:name:address:entrypoints:timezone:).md)
- [convenience init(mapItem: MKMapItem, locationThreshold: Measurement<UnitLength>?, entryPoints: [CPLocationCoordinate3D])](cpnavigationwaypoint/init(mapitem:locationthreshold:entrypoints:).md)
### Instance Properties
- [var address: String?](cpnavigationwaypoint/address.md)
  address is an optional address string for the waypoint, formatted with newline characters separating each address component. Example: “Apple Inc.\n1 Apple Park Way\nCupertino, CA 95014\nUnited States”
- [var centerPoint: CPLocationCoordinate3D](cpnavigationwaypoint/centerpoint.md)
  centerPoint is a CPLocationCoordinate3D representing the primary coordinate location of the waypoint.
- [var entryPoints: [CPLocationCoordinate3D]](cpnavigationwaypoint/entrypoints-obhb.md)
- [var locationThreshold: Measurement<UnitLength>?](cpnavigationwaypoint/locationthreshold.md)
  locationThreshold is the maximum distance in meters from the centerPoint used to determine if a destination is valid.
- [var name: String?](cpnavigationwaypoint/name.md)
  name is an optional display name for the waypoint.
- [var timeZone: TimeZone?](cpnavigationwaypoint/timezone.md)
  The timezone for the waypoint.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint)*