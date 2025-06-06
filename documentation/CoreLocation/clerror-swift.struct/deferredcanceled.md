# deferredCanceled

**Framework**: Core Location  
**Kind**: property

A constant that indicates your app or the location manager canceled the request for deferred updates.

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
static var deferredCanceled: CLError.Code { get }
```

#### Discussion

This error is returned if you call the [`disallowDeferredLocationUpdates()`](cllocationmanager/disallowdeferredlocationupdates().md) method or schedule a new deferred update before the previous deferred update request is processed. The location manager may also report this error too. For example, if the app is in the foreground when a new location is determined, the location manager cancels deferred updates and delivers the location data to your app.

## See Also

- [static var deferredFailed: CLError.Code](clerror-swift.struct/deferredfailed.md)
  A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [static var deferredAccuracyTooLow: CLError.Code](clerror-swift.struct/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [static var deferredDistanceFiltered: CLError.Code](clerror-swift.struct/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [static var deferredNotUpdatingLocation: CLError.Code](clerror-swift.struct/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/deferredcanceled)*