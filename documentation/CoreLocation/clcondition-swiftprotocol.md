# CLCondition

**Framework**: Core Location  
**Kind**: protocol

The abstract base class for all other monitor conditions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
protocol CLCondition : Decodable, Encodable, Sendable
```

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [CLMonitor.BeaconIdentityCondition](clmonitor-2r51v/beaconidentitycondition.md)
- [CLMonitor.CircularGeographicCondition](clmonitor-2r51v/circulargeographiccondition.md)

## See Also

- [Ranging for Beacons](ranging-for-beacons.md)
  Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)
  Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md)
  Broadcast iBeacon signals from an iOS device.
- [class CLBeacon](clbeacon.md)
  Information about an observed iBeacon device and its relative distance to a person’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcondition-swift.protocol)*