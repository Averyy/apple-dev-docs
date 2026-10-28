# CLMonitor.BeaconIdentityCondition

**Framework**: Core Location  
**Kind**: struct  
**Role**: Structure

A condition that describes the characteristics of a beacon.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
struct BeaconIdentityCondition
```

## Overview

Use `CLMonitor.BeaconIdentityCondition` to observe events from beacons based on any combination on their UUID, major, or minor characteristics.

## Topics

### Creating a beacon identity condition
- [init(uuid: UUID)](./beaconidentitycondition/init%28uuid%29.md)
  Creates a beacon identity condition with the UUID characteristic only, and wildcard values for the major and minor characteristics.
- [init(uuid: UUID, major: UInt16)](./beaconidentitycondition/init%28uuid,major%29.md)
  Creates a beacon identity condition with UUID and major characteristics, and a wildcard for the minor characteristic.
- [init(uuid: UUID, major: UInt16, minor: UInt16)](./beaconidentitycondition/init%28uuid,major,minor%29.md)
  Creates a beacon identity condition with UUID, and major and minor characteristics.
### Instance Properties
- [let major: UInt16?](./beaconidentitycondition/major.md)
- [let minor: UInt16?](./beaconidentitycondition/minor.md)
- [let uuid: UUID](./beaconidentitycondition/uuid.md)

## Relationships

### Conforms To
- [CLCondition](../clcondition-swift.protocol.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitor conditions
- [CLMonitor.CircularGeographicCondition](./circulargeographiccondition.md)
  A condition that describes a circular geographic area that a center point and radius define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition)*