# CLBeaconRegion

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

A region for detecting the presence of iBeacon devices.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use [`CLBeaconIdentityCondition`](./clbeaconidentitycondition.md) instead.

## Declaration

```swift
class CLBeaconRegion
```

```objc
@interface CLBeaconRegion : CLRegion
```

## Mentions

- [Turning an iOS device into an iBeacon device](./turning-an-ios-device-into-an-ibeacon-device.md)
- [Determining the proximity to an iBeacon device](./determining-the-proximity-to-an-ibeacon-device.md)

## Overview

A [`CLBeaconRegion`](./clbeaconregion.md) object defines a region that you use to detect Bluetooth beacons conforming to the iBeacon specification. In contrast to a [`CLCircularRegion`](./clcircularregion.md) that centers on a geographic location, a [`CLBeaconRegion`](./clbeaconregion.md) focuses on an iBeacon with specific identifying characteristics, which you provide. When a matching device comes in range, Core Location notifies your app.

You monitor beacon regions in two ways. To detect when a beacon is in range, use the [`startMonitoring(for:)`](./cllocationmanager/startmonitoring%28for%29.md) method of your location manager object. After detecting a beacon, call the [`startRangingBeacons(in:)`](./cllocationmanager/startrangingbeacons%28in%29.md) method to determine the relative distance to that beacon.

When detecting an iBeacon, you need to specify the [`proximityUUID`](./clbeaconregion/proximityuuid.md), [`major`](./clbeaconregion/major.md), and [`minor`](./clbeaconregion/minor.md) values that you programmed into the beacon hardware. You use the values to identify your beacons uniquely, and you can specify a subset of values to detect multiple beacons. The [`proximityUUID`](./clbeaconregion/proximityuuid.md) property is typically the same for all of the beacons in your installation. Use the [`major`](./clbeaconregion/major.md) and [`minor`](./clbeaconregion/minor.md) values to distinguish among different beacons in your installation.

If you want to configure the current iOS device as a Bluetooth beacon, create a beacon region with the appropriate identifying information. You can then call the [`peripheralData(withMeasuredPower:)`](./clbeaconregion/peripheraldata%28withmeasuredpower%29.md) method of the region to get a dictionary that you can use to advertise the device with the Core Bluetooth framework. For more information about using that framework to advertise the device as a beacon, see [Turning an iOS device into an iBeacon device](./turning-an-ios-device-into-an-ibeacon-device.md).

For information about how to detect beacons, see [Determining the proximity to an iBeacon device](./determining-the-proximity-to-an-ibeacon-device.md).

## Topics

### Creating a beacon region
- [init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)](./clbeaconregion/init%28beaconidentityconstraint,identifier%29.md)
  Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.
- [init(uuid: UUID, identifier: String)](./clbeaconregion/init%28uuid,identifier%29-6hg8v.md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)](./clbeaconregion/init%28uuid,major,identifier%29-8ur0j.md)
  Creates and returns a region object that targets beacons with the specified UUID and major value.
- [init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./clbeaconregion/init%28uuid,major,minor,identifier%29-24h7w.md)
  Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.
- [typealias CLBeaconMajorValue](./clbeaconmajorvalue.md)
  The most significant value in a beacon.
- [typealias CLBeaconMinorValue](./clbeaconminorvalue.md)
  The least significant value in a beacon.
### Getting the beacon identity
- [var uuid: UUID](./clbeaconregion/uuid.md)
  The UUID value from the beacon identity constraint that defines the beacon region.
- [var major: NSNumber?](./clbeaconregion/major.md)
  The major value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](./clbeaconregion/minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](./clbeaconregion/beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.
### Specifying when to send notifications
- [var notifyEntryStateOnDisplay: Bool](./clbeaconregion/notifyentrystateondisplay.md)
  A Boolean value that indicates whether Core Location sends beacon notifications when the device’s display is on.
### Getting the beacon’s advertisement data
- [func peripheralData(withMeasuredPower: NSNumber?) -> NSMutableDictionary](./clbeaconregion/peripheraldata%28withmeasuredpower%29.md)
  Retrieves data that you can use to advertise the current device as a beacon.
### Deprecated
- [init(proximityUUID: UUID, identifier: String)](./clbeaconregion/init%28proximityuuid,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](./clbeaconregion/init%28proximityuuid,major,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./clbeaconregion/init%28proximityuuid,major,minor,identifier%29.md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.
- [var proximityUUID: UUID](./clbeaconregion/proximityuuid.md)
  The unique ID of the beacons you’re targeting.
### Initializers
- [init(UUID: UUID, identifier: String)](./clbeaconregion/init%28uuid,identifier%29-6114g.md)
- [init(UUID: UUID, major: CLBeaconMajorValue, identifier: String)](./clbeaconregion/init%28uuid,major,identifier%29-71t0b.md)
- [init(UUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](./clbeaconregion/init%28uuid,major,minor,identifier%29-9ejej.md)

## Relationships

### Inherits From
- [CLRegion](./clregion.md)
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

### Classes
- [class CLBeaconIdentityConstraint](./clbeaconidentityconstraint.md)
  Identity characteristics that can match one or more beacons.
- [class CLCircularRegion](./clcircularregion.md)
  A circular geographic region that a center point and radius deine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion)*