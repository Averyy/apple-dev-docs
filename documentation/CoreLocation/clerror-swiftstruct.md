# CLError

**Framework**: Core Location  
**Kind**: struct

A Core Location error.

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
struct CLError
```

#### Overview

Instances of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object delivered to the delegate use these error codes for the [`code`](https://developer.apple.com/documentation/Foundation/NSError/code) property of the error object.

## Topics

### Getting general errors
- [static var locationUnknown: CLError.Code](clerror-swift.struct/locationunknown.md)
  A constant that indicates the location manager was unable to obtain a location value right now.
- [static var denied: CLError.Code](clerror-swift.struct/denied.md)
  A constant that indicates the user denied access to the location service.
- [static var promptDeclined: CLError.Code](clerror-swift.struct/promptdeclined.md)
  A constant that indicates the user didn’t grant the requested temporary authorization.
- [static var network: CLError.Code](clerror-swift.struct/network.md)
  A constant that indicates the network was unavailable or a network error occurred.
- [static var headingFailure: CLError.Code](clerror-swift.struct/headingfailure.md)
  A constant that indicates the location manager can’t determine the heading.
- [static var rangingUnavailable: CLError.Code](clerror-swift.struct/rangingunavailable.md)
  A constant that indicates ranging is disabled.
- [static var rangingFailure: CLError.Code](clerror-swift.struct/rangingfailure.md)
  A constant that indicates a general ranging error occurred.
- [CLError.Code](clerror-swift.struct/code.md)
  Error codes returned by the location manager object.
### Getting region monitoring errors
- [static var regionMonitoringDenied: CLError.Code](clerror-swift.struct/regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [static var regionMonitoringFailure: CLError.Code](clerror-swift.struct/regionmonitoringfailure.md)
  A constant that indicates the location manager failed to monitor a registered region.
- [static var regionMonitoringSetupDelayed: CLError.Code](clerror-swift.struct/regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.
- [static var regionMonitoringResponseDelayed: CLError.Code](clerror-swift.struct/regionmonitoringresponsedelayed.md)
  A constant that indicates Core Location will deliver events but they may be delayed.
### Getting geocoding errors
- [static var geocodeCanceled: CLError.Code](clerror-swift.struct/geocodecanceled.md)
  A constant that indicates the geocode request was canceled.
- [static var geocodeFoundNoResult: CLError.Code](clerror-swift.struct/geocodefoundnoresult.md)
  A constant that indicates the geocode request yielded no result.
- [static var geocodeFoundPartialResult: CLError.Code](clerror-swift.struct/geocodefoundpartialresult.md)
  A constant that indicates the geocode request yielded a partial result.
### Getting deferred location update errors
- [static var deferredFailed: CLError.Code](clerror-swift.struct/deferredfailed.md)
  A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [static var deferredCanceled: CLError.Code](clerror-swift.struct/deferredcanceled.md)
  A constant that indicates your app or the location manager canceled the request for deferred updates.
- [static var deferredAccuracyTooLow: CLError.Code](clerror-swift.struct/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [static var deferredDistanceFiltered: CLError.Code](clerror-swift.struct/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [static var deferredNotUpdatingLocation: CLError.Code](clerror-swift.struct/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.
### Getting the error details
- [var alternateRegion: CLRegion?](clerror-swift.struct/alternateregion.md)
  A region that location services can monitor more effectively.
### Type Properties
- [static var historicalLocationError: CLError.Code](clerror-swift.struct/historicallocationerror.md)
- [static var errorDomain: String](clerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let kCLErrorDomain: String](kclerrordomain.md)
  The domain for Core Location errors.
- [let kCLErrorUserInfoAlternateRegionKey: String](kclerroruserinfoalternateregionkey.md)
  A key in the user information dictionary of an error relating to a delayed region-monitoring response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct)*