# CLBeaconIdentityCondition

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

A condition that describes the identity characteristics of a beacon.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@interface CLBeaconIdentityCondition : CLCondition
```

#### Overview

Core Location defines a beacon identity by UUID, and major and minor values. You need to specify the UUID. If you only specify a UUID, the framework treats the major and minor values as wildcards and any beacons with the same UUID satisfy the condition. Similarly, if you specify only a UUID and a major value, the framework treats the minor value as a wildcard and any beacons with the same UUID and major value satisfy the condition.

## Topics

### Creating beacon identity conditions
- [- initWithUUID:](./clbeaconidentitycondition/initwithuuid_.md)
  Creates a new beacon identity condition with the identifier you specify.
- [- initWithUUID:major:](./clbeaconidentitycondition/initwithuuid_major_.md)
  Creates a new beacon identity condition with the identifier and major value you specify.
- [- initWithUUID:major:minor:](./clbeaconidentitycondition/initwithuuid_major_minor_.md)
  Creates a new beacon identity condition with the identifier, and major and minor values you specify.
### Accessing the beacon’s properties
- [UUID](./clbeaconidentitycondition/uuid.md)
  A universally unique identifier that represent the beacon’s identifier.
- [major](./clbeaconidentitycondition/major.md)
  The most significant value associated with the beacon.
- [minor](./clbeaconidentitycondition/minor.md)
  The least significant value associated with the beacon.

## Relationships

### Inherits From
- [CLCondition](./clcondition-c.class.md)
### Inherited By
- [CLBeaconIdentityConstraint](./clbeaconidentityconstraint.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### iBeacon
- [Ranging for Beacons](./ranging-for-beacons.md)
  Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](./determining-the-proximity-to-an-ibeacon-device.md)
  Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](./turning-an-ios-device-into-an-ibeacon-device.md)
  Broadcast iBeacon signals from an iOS device.
- [class CLBeacon](./clbeacon.md)
  Information about an observed iBeacon device and its relative distance to a person’s device.
- [CLCondition](./clcondition-c.class.md)
  The abstract base class that all other conditions derive from.
- [CLCircularGeographicCondition](./clcirculargeographiccondition.md)
  A circular geographic condition that a center point and radius define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconidentitycondition)*