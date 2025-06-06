# deferredFailed

**Framework**: Core Location  
**Kind**: property

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
static var deferredFailed: CLError.Code { get }
```

#### Discussion

This error can occur if GPS is unavailable, not active, or is temporarily interrupted. If you get this error on a device that has GPS hardware, the solution is to try again.

## See Also

- [static var deferredCanceled: CLError.Code](clerror-swift.struct/deferredcanceled.md)
  A constant that indicates your app or the location manager canceled the request for deferred updates.
- [static var deferredAccuracyTooLow: CLError.Code](clerror-swift.struct/deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [static var deferredDistanceFiltered: CLError.Code](clerror-swift.struct/deferreddistancefiltered.md)
  A constant that indicates deferred mode doesn’t support distance filters.
- [static var deferredNotUpdatingLocation: CLError.Code](clerror-swift.struct/deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/deferredfailed)*