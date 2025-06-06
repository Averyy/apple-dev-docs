# CLError.Code.deferredCanceled

**Framework**: Core Location  
**Kind**: case

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
case deferredCanceled
```

#### Discussion

This error is returned if you call the [`disallowDeferredLocationUpdates()`](cllocationmanager/disallowdeferredlocationupdates().md) method or schedule a new deferred update before the previous deferred update request is processed. The location manager may also report this error too. For example, if the app is in the foreground when a new location is determined, the location manager cancels deferred updates and delivers the location data to your app.

## See Also

- [CLError.Code.deferredFailed](clerror-swift.struct/code/deferredfailed.md)
  A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [CLError.Code.deferredAccuracyTooLow](clerror-swift.struct/code/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [CLError.Code.deferredDistanceFiltered](clerror-swift.struct/code/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [CLError.Code.deferredNotUpdatingLocation](clerror-swift.struct/code/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/deferredcanceled)*