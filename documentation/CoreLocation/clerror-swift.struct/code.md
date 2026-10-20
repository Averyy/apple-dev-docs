# CLError.Code

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CLError : NSInteger;
```

#### Overview

Instances of [`NSError`](../../Foundation/nserror.md) object delivered to the delegate use these error codes for the [`code`](../../Foundation/nserror/code.md) property of the error object.

## Topics

### Getting general errors
- [CLError.Code.locationUnknown](./code/locationunknown.md)
  A constant that indicates the location manager was unable to obtain a location value right now.
- [CLError.Code.denied](./code/denied.md)
  A constant that indicates the user denied access to the location service.
- [CLError.Code.promptDeclined](./code/promptdeclined.md)
  A constant that indicates the user didn’t grant the requested temporary authorization.
- [CLError.Code.network](./code/network.md)
  A constant that indicates the network was unavailable or a network error occurred.
- [CLError.Code.headingFailure](./code/headingfailure.md)
  A constant that indicates the location manager can’t determine the heading.
- [CLError.Code.rangingUnavailable](./code/rangingunavailable.md)
  A constant that indicates ranging is disabled.
- [CLError.Code.rangingFailure](./code/rangingfailure.md)
  A constant that indicates a general ranging error occurred.
### Getting region monitoring errors
- [CLError.Code.regionMonitoringDenied](./code/regionmonitoringdenied.md)
  A constant that indicates the user denied access to the region monitoring service.
- [CLError.Code.regionMonitoringFailure](./code/regionmonitoringfailure.md)
  A constant that indicates the location manager failed to monitor a registered region.
- [CLError.Code.regionMonitoringSetupDelayed](./code/regionmonitoringsetupdelayed.md)
  A constant that indicates Core Location failed to initialize the region monitoring feature.
- [CLError.Code.regionMonitoringResponseDelayed](./code/regionmonitoringresponsedelayed.md)
  A constant that indicates Core Location will deliver events but they may be delayed.
### Getting geocoding errors
- [CLError.Code.geocodeCanceled](./code/geocodecanceled.md)
  A constant that indicates the geocode request was canceled.
- [CLError.Code.geocodeFoundNoResult](./code/geocodefoundnoresult.md)
  A constant that indicates the geocode request yielded no result.
- [CLError.Code.geocodeFoundPartialResult](./code/geocodefoundpartialresult.md)
  A constant that indicates the geocode request yielded a partial result.
### Getting deferred location update errors
- [CLError.Code.deferredFailed](./code/deferredfailed.md)
  A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [CLError.Code.deferredCanceled](./code/deferredcanceled.md)
  A constant that indicates your app or the location manager canceled the request for deferred updates.
- [CLError.Code.deferredAccuracyTooLow](./code/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [CLError.Code.deferredDistanceFiltered](./code/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [CLError.Code.deferredNotUpdatingLocation](./code/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.
### Enumeration cases
- [CLError.Code.historicalLocationError](./code/historicallocationerror.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting general errors
- [static var locationUnknown: CLError.Code](./locationunknown.md)
  A constant that indicates the location manager was unable to obtain a location value right now.
- [static var denied: CLError.Code](./denied.md)
  A constant that indicates the user denied access to the location service.
- [static var promptDeclined: CLError.Code](./promptdeclined.md)
  A constant that indicates the user didn’t grant the requested temporary authorization.
- [static var network: CLError.Code](./network.md)
  A constant that indicates the network was unavailable or a network error occurred.
- [static var headingFailure: CLError.Code](./headingfailure.md)
  A constant that indicates the location manager can’t determine the heading.
- [static var rangingUnavailable: CLError.Code](./rangingunavailable.md)
  A constant that indicates ranging is disabled.
- [static var rangingFailure: CLError.Code](./rangingfailure.md)
  A constant that indicates a general ranging error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code)*