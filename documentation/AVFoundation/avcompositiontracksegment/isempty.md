# isEmpty

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isEmpty) BOOL empty;
```

## Discussion

An empty segment has a valid target time range, but its [`sourceURL`](./sourceurl.md) value is `nil` and the source start time is [`invalid`](../../CoreMedia/cmtime/invalid.md). It doesn’t set values for its other properties.

## See Also

### Accessing segment properties
- [var sourceURL: URL?](./sourceurl.md)
  A URL of the container file whose media this track segment presents.
- [var sourceTrackID: CMPersistentTrackID](./sourcetrackid.md)
  An identifier of a track in the container file whose media this track segment presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/isempty)*