# CLCondition

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

The abstract base class that all other conditions derive from.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@interface CLCondition : NSObject
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CLBeaconIdentityCondition](./clbeaconidentitycondition.md)
- [CLCircularGeographicCondition](./clcirculargeographiccondition.md)
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
- [CLBeaconIdentityCondition](./clbeaconidentitycondition.md)
  A condition that describes the identity characteristics of a beacon.
- [CLCircularGeographicCondition](./clcirculargeographiccondition.md)
  A circular geographic condition that a center point and radius define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcondition-c.class)*