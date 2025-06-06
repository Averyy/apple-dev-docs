# CLError.Code.regionMonitoringFailure

**Framework**: Core Location  
**Kind**: case

A constant that indicates the location manager failed to monitor a registered region.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case regionMonitoringFailure
```

#### Discussion

Monitoring can fail if the app exceeds the maximum number of regions that it can monitor simultaneously. Monitoring can also fail if the region’s radius distance is too large.

## See Also

- [CLError.Code.regionMonitoringDenied](clerror-swift.struct/code/regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [CLError.Code.regionMonitoringSetupDelayed](clerror-swift.struct/code/regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location failed to initialize the region monitoring feature.
- [CLError.Code.regionMonitoringResponseDelayed](clerror-swift.struct/code/regionmonitoringresponsedelayed.md)
  A constant that indicates Core Location will deliver events but they may be delayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/regionmonitoringfailure)*