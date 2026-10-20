# CPNavigationWaypoint

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

CPNavigationWaypoint represents a point of interest along a route that provides location-based information and guidance.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class CPNavigationWaypoint
```

```objc
@interface CPNavigationWaypoint : NSObject
```

## Topics

### Initializers
- [convenience init(centerPoint: CPLocationCoordinate3D, locationThreshold: Measurement<UnitLength>?, name: String?, address: String?, entryPoints: [CPLocationCoordinate3D], timeZone: TimeZone?)](./cpnavigationwaypoint/init%28centerpoint,locationthreshold,name,address,entrypoints,timezone%29.md)
- [convenience init(centerPoint: CPLocationCoordinate3D, locationThreshold: Measurement<UnitLength>?, nameVariants: [String], addressVariants: [String], entryPoints: [CPLocationCoordinate3D], timeZone: TimeZone?)](./cpnavigationwaypoint/init%28centerpoint,locationthreshold,namevariants,addressvariants,entrypoints,timezone%29.md)
- [init?(coder: NSCoder)](./cpnavigationwaypoint/init%28coder%29.md)
- [convenience init(mapItem: MKMapItem, locationThreshold: Measurement<UnitLength>?, entryPoints: [CPLocationCoordinate3D])](./cpnavigationwaypoint/init%28mapitem,locationthreshold,entrypoints%29.md)
### Instance Properties
- [var address: String?](./cpnavigationwaypoint/address.md)
  address is an optional address string for the waypoint, formatted with newline characters separating each address component. Example: “Apple Inc.\n1 Apple Park Way\nCupertino, CA 95014\nUnited States”
- [var addressVariants: [String]](./cpnavigationwaypoint/addressvariants.md)
  addressVariants is an array of @c NSString representing variants of the waypoint’s address, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.
- [var centerPoint: CPLocationCoordinate3D](./cpnavigationwaypoint/centerpoint.md)
  centerPoint is a CPLocationCoordinate3D representing the primary coordinate location of the waypoint.
- [var entryPoints: [CPLocationCoordinate3D]](./cpnavigationwaypoint/entrypoints-obhb.md)
- [var locationThreshold: Measurement<UnitLength>?](./cpnavigationwaypoint/locationthreshold.md)
  locationThreshold is the maximum distance in meters from the centerPoint used to determine if a destination is valid.
- [var name: String?](./cpnavigationwaypoint/name.md)
  name is an optional display name for the waypoint.
- [var nameVariants: [String]](./cpnavigationwaypoint/namevariants.md)
  nameVariants is an array of @c NSString representing variants of the waypoint’s display name, arranged from most to least preferred. The variant strings should be provided as localized, displayable content.
- [var timeZone: TimeZone?](./cpnavigationwaypoint/timezone.md)
  The timezone for the waypoint.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint)*