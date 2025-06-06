# CLError.Code.regionMonitoringResponseDelayed

**Framework**: Core Location  
**Kind**: case

A constant that indicates Core Location will deliver events but they may be delayed.

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
case regionMonitoringResponseDelayed
```

#### Discussion

The user information dictionary might contain an alternate region that you can monitor instead. Use [`kCLErrorUserInfoAlternateRegionKey`](kclerroruserinfoalternateregionkey.md) to retrieve the [`CLRegion`](clregion.md) object.

## See Also

- [CLError.Code.regionMonitoringDenied](clerror-swift.struct/code/regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [CLError.Code.regionMonitoringFailure](clerror-swift.struct/code/regionmonitoringfailure.md)
  A constant that indicates the location manager failed to monitor a registered region.
- [CLError.Code.regionMonitoringSetupDelayed](clerror-swift.struct/code/regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location failed to initialize the region monitoring feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/regionmonitoringresponsedelayed)*