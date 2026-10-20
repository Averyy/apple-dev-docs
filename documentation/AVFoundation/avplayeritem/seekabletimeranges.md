# seekableTimeRanges

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of time ranges within which it is possible to seek.

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
var seekableTimeRanges: [NSValue] { get }
```

```objc
@property (readonly) NSArray<NSValue *> * seekableTimeRanges;
```

#### Discussion

The array contains [`NSValue`](../../Foundation/nsvalue.md) objects containing a [`CMTimeRange`](../../CoreMedia/cmtimerange.md) value indicating the times ranges to which the player item can seek. The time ranges returned may be discontinuous.

## See Also

### Determining available time ranges
- [var loadedTimeRanges: [NSValue]](./loadedtimeranges.md)
  An array of time ranges indicating media data that is readily available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seekabletimeranges)*