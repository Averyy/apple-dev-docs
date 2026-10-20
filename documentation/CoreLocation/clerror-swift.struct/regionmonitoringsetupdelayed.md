# regionMonitoringSetupDelayed

**Framework**: Core Location  
**Kind**: property  
**Role**: Type Property

A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.

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
static var regionMonitoringSetupDelayed: CLError.Code { get }
```

## See Also

### Getting region monitoring errors
- [static var regionMonitoringDenied: CLError.Code](./regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [static var regionMonitoringFailure: CLError.Code](./regionmonitoringfailure.md)
  A constant that indicates the location manager failed to monitor a registered region.
- [static var regionMonitoringResponseDelayed: CLError.Code](./regionmonitoringresponsedelayed.md)
  A constant that indicates Core Location will deliver events but they may be delayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/regionmonitoringsetupdelayed)*