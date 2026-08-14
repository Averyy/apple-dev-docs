# CLBeacon

**Framework**: Core Location  
**Kind**: class

Information about an observed iBeacon device and its relative distance to a person’s device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
class CLBeacon
```

## Mentions

- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md)

#### Overview

The [`CLBeacon`](clbeacon.md) class represents a beacon that was observed during beacon ranging. You do not create instances of this class directly. The location manager ([`CLLocationManager`](cllocationmanager.md)) object reports observed beacons to its associated delegate object.

The identity of a beacon is defined by its [`uuid`](clbeacon/uuid.md), [`major`](clbeacon/major.md), and [`minor`](clbeacon/minor.md) properties. These values are coded into the beacon itself. For a more thorough description of the meaning of those values, see [`CLBeaconRegion`](clbeaconregion.md).

## Topics

### Getting the beacon identity
- [var uuid: UUID](clbeacon/uuid.md)
  The UUID that the observed beacon transmitted.
- [var major: NSNumber](clbeacon/major.md)
  The major value that the observed beacon transmitted.
- [var minor: NSNumber](clbeacon/minor.md)
  The minor value that the observed beacon transmitted.
- [var proximityUUID: UUID](clbeacon/proximityuuid.md)
  The proximity ID of the beacon.
### Determining the distance to the beacon
- [var proximity: CLProximity](clbeacon/proximity.md)
  The relative distance to the beacon.
- [enum CLProximity](clproximity.md)
  Constants that reflect the relative distance to a beacon.
- [var accuracy: CLLocationAccuracy](clbeacon/accuracy.md)
  The accuracy of the proximity value, measured in meters from the beacon.
- [var rssi: Int](clbeacon/rssi.md)
  The received signal strength of the beacon, measured in decibels.
### Getting the observation timestamp
- [var timestamp: Date](clbeacon/timestamp.md)
  A timestamp representing when the beacon was observed.
### Initializers
- [init?(coder: NSCoder)](clbeacon/init(coder:).md)

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
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Ranging for Beacons](ranging-for-beacons.md)
  Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)
  Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md)
  Broadcast iBeacon signals from an iOS device.
- [protocol CLCondition](clcondition-swift.protocol.md)
  The abstract base class for all other monitor conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeacon)*