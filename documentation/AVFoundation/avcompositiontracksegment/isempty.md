# isEmpty

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the segment is empty.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

An empty segment has a valid target time range, but its [`sourceURL`](avcompositiontracksegment/sourceurl.md) value is `nil` and the source start time is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid). It doesn’t set values for its other properties.

## See Also

- [var sourceURL: URL?](avcompositiontracksegment/sourceurl.md)
  A URL of the container file whose media this track segment presents.
- [var sourceTrackID: CMPersistentTrackID](avcompositiontracksegment/sourcetrackid.md)
  An identifier of a track in the container file whose media this track segment presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/isempty)*