# maximumRegionMonitoringDistance

**Framework**: Core Location  
**Kind**: property

The largest boundary distance that can be assigned to a region.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var maximumRegionMonitoringDistance: CLLocationDistance { get }
```

#### Discussion

This property defines the largest boundary distance allowed from a region’s center point. Attempting to monitor a region with a distance larger than this value causes the location manager to send a [`CLError.Code.regionMonitoringFailure`](clerror-swift.struct/code/regionmonitoringfailure.md) error to the delegate.

If region monitoring is unavailable or not supported, the value in this property is `-1`.

## See Also

- [var monitoredRegions: Set<CLRegion>](cllocationmanager/monitoredregions.md)
  The set of shared regions monitored by all location-manager objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/maximumregionmonitoringdistance)*