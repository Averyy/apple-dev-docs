# CPRouteSource

**Framework**: CarPlay  
**Kind**: enum

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
enum CPRouteSource
```

#### Overview

Specifies the destination and modification status of route information displayed to the user

## Topics

### Enumeration Cases
- [CPRouteSource.sourceInactive](cproutesource/sourceinactive.md)
  No current route source.
- [CPRouteSource.sourceVehicle](cproutesource/sourcevehicle.md)
  Route and destination(s) being used by the vehicle is from the vehicle’s system.
- [CPRouteSource.sourceiOSDestinationsOnly](cproutesource/sourceiosdestinationsonly.md)
  Only the destination(s) from the device are being used, routes are not.
- [CPRouteSource.sourceiOSRouteDestinationsModified](cproutesource/sourceiosroutedestinationsmodified.md)
  Route and destination(s) from the device are being used but both have been modified.
- [CPRouteSource.sourceiOSRouteModified](cproutesource/sourceiosroutemodified.md)
  Route is from the device and being used by the vehicle but has been modified. The destination(s)/waypoints have not been changed.
- [CPRouteSource.sourceiOSUnchanged](cproutesource/sourceiosunchanged.md)
  Route is from the device and being used by the vehicle unmodified.
### Initializers
- [init?(rawValue: UInt)](cproutesource/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutesource)*