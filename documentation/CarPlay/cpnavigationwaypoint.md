# CPNavigationWaypoint

**Framework**: CarPlay  
**Kind**: class

CPNavigationWaypoint represents a point of interest along a route that provides location-based information and guidance.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class CPNavigationWaypoint
```

## Topics

### Initializers
- [convenience init(centerPoint: CPLocationCoordinate3D, locationThreshold: Measurement<UnitLength>?, name: String?, address: String?, entryPoints: [CPLocationCoordinate3D], timeZone: TimeZone?)](cpnavigationwaypoint/init(centerpoint:locationthreshold:name:address:entrypoints:timezone:).md)
- [convenience init(centerPoint: CPLocationCoordinate3D, locationThreshold: Measurement<UnitLength>?, nameVariants: [String], addressVariants: [String], entryPoints: [CPLocationCoordinate3D], timeZone: TimeZone?)](cpnavigationwaypoint/init(centerpoint:locationthreshold:namevariants:addressvariants:entrypoints:timezone:).md)
- [init?(coder: NSCoder)](cpnavigationwaypoint/init(coder:).md)
- [convenience init(mapItem: MKMapItem, locationThreshold: Measurement<UnitLength>?, entryPoints: [CPLocationCoordinate3D])](cpnavigationwaypoint/init(mapitem:locationthreshold:entrypoints:).md)
### Instance Properties
- [var address: String?](cpnavigationwaypoint/address.md)
  address is an optional address string for the waypoint, formatted with newline characters separating each address component. Example: “Apple Inc.\n1 Apple Park Way\nCupertino, CA 95014\nUnited States”
- [var addressVariants: [String]](cpnavigationwaypoint/addressvariants.md)
  addressVariants is an array of @c NSString representing variants of the waypoint’s address, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.
- [var centerPoint: CPLocationCoordinate3D](cpnavigationwaypoint/centerpoint.md)
  centerPoint is a CPLocationCoordinate3D representing the primary coordinate location of the waypoint.
- [var entryPoints: [CPLocationCoordinate3D]](cpnavigationwaypoint/entrypoints-obhb.md)
- [var locationThreshold: Measurement<UnitLength>?](cpnavigationwaypoint/locationthreshold.md)
  locationThreshold is the maximum distance in meters from the centerPoint used to determine if a destination is valid.
- [var name: String?](cpnavigationwaypoint/name.md)
  name is an optional display name for the waypoint.
- [var nameVariants: [String]](cpnavigationwaypoint/namevariants.md)
  nameVariants is an array of @c NSString representing variants of the waypoint’s display name, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.
- [var timeZone: TimeZone?](cpnavigationwaypoint/timezone.md)
  The timezone for the waypoint.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint)*