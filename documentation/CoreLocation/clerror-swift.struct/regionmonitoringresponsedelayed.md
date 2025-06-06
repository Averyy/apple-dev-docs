# regionMonitoringResponseDelayed

**Framework**: Core Location  
**Kind**: property

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
static var regionMonitoringResponseDelayed: CLError.Code { get }
```

#### Discussion

The user information dictionary might contain an alternate region that you can monitor instead. Use the [`alternateRegion`](clerror-swift.struct/alternateregion.md) property to retrieve the [`CLRegion`](clregion.md) object.

## See Also

- [static var regionMonitoringDenied: CLError.Code](clerror-swift.struct/regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [static var regionMonitoringFailure: CLError.Code](clerror-swift.struct/regionmonitoringfailure.md)
  A constant that indicates the location manager failed to monitor a registered region.
- [static var regionMonitoringSetupDelayed: CLError.Code](clerror-swift.struct/regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/regionmonitoringresponsedelayed)*