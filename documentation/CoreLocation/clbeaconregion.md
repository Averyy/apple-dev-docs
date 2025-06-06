# CLBeaconRegion

**Framework**: Core Location  
**Kind**: class

A region for detecting the presence of iBeacon devices.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
class CLBeaconRegion
```

## Mentions

- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md)
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)

#### Overview

A [`CLBeaconRegion`](clbeaconregion.md) object defines a region that you use to detect Bluetooth beacons conforming to the iBeacon specification. In contrast to a [`CLCircularRegion`](clcircularregion.md) that centers on a geographic location, a [`CLBeaconRegion`](clbeaconregion.md) focuses on an iBeacon with specific identifying characteristics, which you provide. When a matching device comes in range, Core Location notifies your app.

You monitor beacon regions in two ways. To detect when a beacon is in range, use the [`startMonitoring(for:)`](cllocationmanager/startmonitoring(for:).md) method of your location manager object. After detecting a beacon, call the [`startRangingBeacons(in:)`](cllocationmanager/startrangingbeacons(in:).md) method to determine the relative distance to that beacon.

When detecting an iBeacon, you need to specify the [`proximityUUID`](clbeaconregion/proximityuuid.md), [`major`](clbeaconregion/major.md), and [`minor`](clbeaconregion/minor.md) values that you programmed into the beacon hardware. You use the values to identify your beacons uniquely, and you can specify a subset of values to detect multiple beacons. The [`proximityUUID`](clbeaconregion/proximityuuid.md) property is typically the same for all of the beacons in your installation. Use the [`major`](clbeaconregion/major.md) and [`minor`](clbeaconregion/minor.md) values to distinguish among different beacons in your installation.

If you want to configure the current iOS device as a Bluetooth beacon, create a beacon region with the appropriate identifying information. You can then call the [`peripheralData(withMeasuredPower:)`](clbeaconregion/peripheraldata(withmeasuredpower:).md) method of the region to get a dictionary that you can use to advertise the device with the Core Bluetooth framework. For more information about using that framework to advertise the device as a beacon, see [`Turning an iOS device into an iBeacon device`](turning-an-ios-device-into-an-ibeacon-device.md).

For information about how to detect beacons, see [`Determining the proximity to an iBeacon device`](determining-the-proximity-to-an-ibeacon-device.md).

## Topics

### Creating a beacon region
- [init(beaconIdentityConstraint: CLBeaconIdentityConstraint, identifier: String)](clbeaconregion/init(beaconidentityconstraint:identifier:).md)
  Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints.
- [init(uuid: UUID, identifier: String)](clbeaconregion/init(uuid:identifier:).md)
  Creates and returns a region object that targets beacons with the specified UUID.
- [init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(uuid:major:identifier:).md)
  Creates and returns a region object that targets beacons with the specified UUID and major value.
- [init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(uuid:major:minor:identifier:).md)
  Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.
- [typealias CLBeaconMajorValue](clbeaconmajorvalue.md)
  The most significant value in a beacon.
- [typealias CLBeaconMinorValue](clbeaconminorvalue.md)
  The least significant value in a beacon.
### Getting the beacon identity
- [var uuid: UUID](clbeaconregion/uuid.md)
  The UUID value from the beacon identity constraint that defines the beacon region.
- [var major: NSNumber?](clbeaconregion/major.md)
  The major value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](clbeaconregion/minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](clbeaconregion/beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.
### Specifying when to send notifications
- [var notifyEntryStateOnDisplay: Bool](clbeaconregion/notifyentrystateondisplay.md)
  A Boolean value that indicates whether Core Location sends beacon notifications when the device’s display is on.
### Getting the beacon’s advertisement data
- [func peripheralData(withMeasuredPower: NSNumber?) -> NSMutableDictionary](clbeaconregion/peripheraldata(withmeasuredpower:).md)
  Retrieves data that you can use to advertise the current device as a beacon.
### Deprecated
- [init(proximityUUID: UUID, identifier: String)](clbeaconregion/init(proximityuuid:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified UUID.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID and major value.
- [init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)](clbeaconregion/init(proximityuuid:major:minor:identifier:).md)
  Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.
- [var proximityUUID: UUID](clbeaconregion/proximityuuid.md)
  The unique ID of the beacons you’re targeting.

## Relationships

### Inherits From
- [CLRegion](clregion.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CLBeaconIdentityConstraint](clbeaconidentityconstraint.md)
  Identity characteristics that can match one or more beacons.
- [class CLCircularRegion](clcircularregion.md)
  A circular geographic region that a center point and radius deine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion)*