# CLError.Code

**Framework**: Core Location  
**Kind**: enum

Error codes returned by the location manager object.

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
enum Code
```

#### Overview

Instances of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object delivered to the delegate use these error codes for the [`code`](https://developer.apple.com/documentation/foundation/nserror/1409165-code) property of the error object.

## Topics

### Getting general errors
- [CLError.Code.locationUnknown](clerror-swift.struct/code/locationunknown.md)
  A constant that indicates the location manager was unable to obtain a location value right now.
- [CLError.Code.denied](clerror-swift.struct/code/denied.md)
  A constant that indicates the user denied access to the location service.
- [CLError.Code.promptDeclined](clerror-swift.struct/code/promptdeclined.md)
  A constant that indicates the user didn’t grant the requested temporary authorization.
- [CLError.Code.network](clerror-swift.struct/code/network.md)
  A constant that indicates the network was unavailable or a network error occurred.
- [CLError.Code.headingFailure](clerror-swift.struct/code/headingfailure.md)
  A constant that indicates the location manager can’t determine the heading.
- [CLError.Code.rangingUnavailable](clerror-swift.struct/code/rangingunavailable.md)
  A constant that indicates ranging is disabled.
- [CLError.Code.rangingFailure](clerror-swift.struct/code/rangingfailure.md)
  A constant that indicates a general ranging error occurred.
### Getting region monitoring errors
- [CLError.Code.regionMonitoringDenied](clerror-swift.struct/code/regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [CLError.Code.regionMonitoringFailure](clerror-swift.struct/code/regionmonitoringfailure.md)
  A constant that indicates the location manager failed to monitor a registered region.
- [CLError.Code.regionMonitoringSetupDelayed](clerror-swift.struct/code/regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location failed to initialize the region monitoring feature.
- [CLError.Code.regionMonitoringResponseDelayed](clerror-swift.struct/code/regionmonitoringresponsedelayed.md)
  A constant that indicates Core Location will deliver events but they may be delayed.
### Getting geocoding errors
- [CLError.Code.geocodeCanceled](clerror-swift.struct/code/geocodecanceled.md)
  A constant that indicates the geocode request was canceled.
- [CLError.Code.geocodeFoundNoResult](clerror-swift.struct/code/geocodefoundnoresult.md)
  A constant that indicates the geocode request yielded no result.
- [CLError.Code.geocodeFoundPartialResult](clerror-swift.struct/code/geocodefoundpartialresult.md)
  A constant that indicates the geocode request yielded a partial result.
### Getting deferred location update errors
- [CLError.Code.deferredFailed](clerror-swift.struct/code/deferredfailed.md)
  A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [CLError.Code.deferredCanceled](clerror-swift.struct/code/deferredcanceled.md)
  A constant that indicates your app or the location manager canceled the request for deferred updates.
- [CLError.Code.deferredAccuracyTooLow](clerror-swift.struct/code/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [CLError.Code.deferredDistanceFiltered](clerror-swift.struct/code/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [CLError.Code.deferredNotUpdatingLocation](clerror-swift.struct/code/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.
### Enumeration cases
- [CLError.Code.historicalLocationError](clerror-swift.struct/code/historicallocationerror.md)
### Initializers
- [init?(rawValue: Int)](clerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code)*