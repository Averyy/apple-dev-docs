# rangedRegions

**Framework**: Core Location  
**Kind**: property

The set of regions currently being tracked using ranging.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var rangedRegions: Set<CLRegion> { get }
```

#### Discussion

The objects in the set are instances of the [`CLBeaconRegion`](clbeaconregion.md) class.

## Topics

### Related Documentation
- [func startRangingBeacons(in: CLBeaconRegion)](cllocationmanager/startrangingbeacons(in:).md)
  Starts the delivery of notifications for the specified beacon region.

## See Also

- [var headingAvailable: Bool](cllocationmanager/headingavailable-swift.property.md)
  A Boolean value indicating whether the location manager is able to generate heading-related events.
- [var locationServicesEnabled: Bool](cllocationmanager/locationservicesenabled-swift.property.md)
  A Boolean value indicating whether location services are enabled on the device.
- [var purpose: String?](cllocationmanager/purpose.md)
  An app-provided string that describes the reason for using location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/rangedregions)*