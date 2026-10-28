# rangedRegions

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The set of regions currently being tracked using ranging.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use [`rangedBeaconConstraints`](./rangedbeaconconstraints.md) instead.

## Declaration

```swift
var rangedRegions: Set<CLRegion> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<__kindof CLRegion *> * rangedRegions;
```

## Discussion

The objects in the set are instances of the [`CLBeaconRegion`](../clbeaconregion.md) class.

## Topics

### Related documentation
- [func startRangingBeacons(in: CLBeaconRegion)](./startrangingbeacons%28in%29.md)
  Starts the delivery of notifications for the specified beacon region.

## See Also

### Properties
- [var headingAvailable: Bool](./headingavailable-swift.property.md)
  A Boolean value indicating whether the location manager is able to generate heading-related events.
- [var locationServicesEnabled: Bool](./locationservicesenabled-swift.property.md)
  A Boolean value indicating whether location services are enabled on the device.
- [var purpose: String?](./purpose.md)
  An app-provided string that describes the reason for using location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/rangedregions)*