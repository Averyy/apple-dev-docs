# regionMonitoringFailure

**Framework**: Core Location  
**Kind**: property  
**Role**: Type Property

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
static var regionMonitoringFailure: CLError.Code { get }
```

#### Discussion

Monitoring can fail if the app exceeds the maximum number of regions that it can monitor simultaneously. Monitoring can also fail if the region’s radius distance is too large.

## See Also

### Getting region monitoring errors
- [static var regionMonitoringDenied: CLError.Code](./regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [static var regionMonitoringSetupDelayed: CLError.Code](./regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.
- [static var regionMonitoringResponseDelayed: CLError.Code](./regionmonitoringresponsedelayed.md)
  A constant that indicates Core Location will deliver events but they may be delayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/regionmonitoringfailure)*