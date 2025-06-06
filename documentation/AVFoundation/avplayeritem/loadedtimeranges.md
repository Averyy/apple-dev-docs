# loadedTimeRanges

**Framework**: AVFoundation  
**Kind**: property

An array of time ranges indicating media data that is readily available.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
var loadedTimeRanges: [NSValue] { get }
```

#### Discussion

The array contains [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects containing a [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) value indicating the times ranges for which the player item has media data readily available. The time ranges returned may be discontinuous.

## See Also

- [var seekableTimeRanges: [NSValue]](avplayeritem/seekabletimeranges.md)
  An array of time ranges within which it is possible to seek.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/loadedtimeranges)*