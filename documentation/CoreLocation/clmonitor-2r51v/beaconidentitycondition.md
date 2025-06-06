# CLMonitor.BeaconIdentityCondition

**Framework**: Core Location  
**Kind**: struct

A condition that describes the characteristics of a beacon.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
struct BeaconIdentityCondition
```

#### Overview

Use `CLMonitor.BeaconIdentityCondition` to observe events from beacons based on any combination on their UUID, major, or minor characteristics.

## Topics

### Creating a beacon identity condition
- [init(uuid: UUID)](clmonitor-2r51v/beaconidentitycondition/init(uuid:).md)
  Creates a beacon identity condition with the UUID characteristic only, and wildcard values for the major and minor characteristics.
- [init(uuid: UUID, major: UInt16)](clmonitor-2r51v/beaconidentitycondition/init(uuid:major:).md)
  Creates a beacon identity condition with UUID and major characteristics, and a wildcard for the minor characteristic.
- [init(uuid: UUID, major: UInt16, minor: UInt16)](clmonitor-2r51v/beaconidentitycondition/init(uuid:major:minor:).md)
  Creates a beacon identity condition with UUID, and major and minor characteristics.
### Instance Properties
- [let major: UInt16?](clmonitor-2r51v/beaconidentitycondition/major.md)
- [let minor: UInt16?](clmonitor-2r51v/beaconidentitycondition/minor.md)
- [let uuid: UUID](clmonitor-2r51v/beaconidentitycondition/uuid.md)

## Relationships

### Conforms To
- [CLCondition](clcondition-swift.protocol.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CLMonitor.CircularGeographicCondition](clmonitor-2r51v/circulargeographiccondition.md)
  A condition that describes a circular geographic area that a center point and radius define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition)*