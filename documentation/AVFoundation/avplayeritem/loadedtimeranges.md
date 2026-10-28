# loadedTimeRanges

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of time ranges indicating media data that is readily available.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
var loadedTimeRanges: [NSValue] { get }
```

```objc
@property (readonly) NSArray<NSValue *> * loadedTimeRanges;
```

## Discussion

The array contains [`NSValue`](../../Foundation/nsvalue.md) objects containing a [`CMTimeRange`](../../CoreMedia/cmtimerange.md) value indicating the times ranges for which the player item has media data readily available. The time ranges returned may be discontinuous.

## See Also

### Determining available time ranges
- [var seekableTimeRanges: [NSValue]](./seekabletimeranges.md)
  An array of time ranges within which it is possible to seek.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/loadedtimeranges)*