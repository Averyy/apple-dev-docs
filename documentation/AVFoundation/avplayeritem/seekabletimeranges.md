# seekableTimeRanges

**Framework**: AVFoundation  
**Kind**: property

An array of time ranges within which it is possible to seek.

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
var seekableTimeRanges: [NSValue] { get }
```

#### Discussion

The array contains [`NSValue`](https://developer.apple.com/documentation/foundation/nsvalue) objects containing a [`CMTimeRange`](https://developer.apple.com/documentation/coremedia/cmtimerange) value indicating the times ranges to which the player item can seek. The time ranges returned may be discontinuous.

## See Also

- [var loadedTimeRanges: [NSValue]](avplayeritem/loadedtimeranges.md)
  An array of time ranges indicating media data that is readily available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seekabletimeranges)*