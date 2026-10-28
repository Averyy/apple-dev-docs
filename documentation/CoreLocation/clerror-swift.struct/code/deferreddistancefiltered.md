# CLError.Code.deferredDistanceFiltered

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

A constant that indicates deferred mode doesn’t support distance filters.

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
case deferredDistanceFiltered
```

```c
kCLErrorDeferredDistanceFiltered
```

## Discussion

Set the distance filter to [`kCLDistanceFilterNone`](../../kcldistancefilternone.md).

## See Also

### Getting deferred location update errors
- [CLError.Code.deferredFailed](./deferredfailed.md)
  A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [CLError.Code.deferredCanceled](./deferredcanceled.md)
  A constant that indicates your app or the location manager canceled the request for deferred updates.
- [CLError.Code.deferredAccuracyTooLow](./deferredaccuracytoolow.md)
  A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [CLError.Code.deferredNotUpdatingLocation](./deferrednotupdatinglocation.md)
  A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/deferreddistancefiltered)*