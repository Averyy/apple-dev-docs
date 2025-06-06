# CLError.Code.deferredFailed

**Framework**: Core Location  
**Kind**: case

A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.

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
case deferredFailed
```

#### Discussion

This error can occur if GPS is unavailable, not active, or is temporarily interrupted. If you get this error on a device that has GPS hardware, the solution is to try again.

## See Also

- [CLError.Code.deferredCanceled](clerror-swift.struct/code/deferredcanceled.md)
  A constant that indicates your app or the location manager canceled the request for deferred updates.
- [CLError.Code.deferredAccuracyTooLow](clerror-swift.struct/code/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [CLError.Code.deferredDistanceFiltered](clerror-swift.struct/code/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [CLError.Code.deferredNotUpdatingLocation](clerror-swift.struct/code/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/deferredfailed)*