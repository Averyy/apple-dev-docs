# mediaDataStorage

**Framework**: AVFoundation  
**Kind**: property

The storage container for media data added to a track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var mediaDataStorage: AVMediaDataStorage? { get }
```

#### Discussion

The value of this property is an [`AVMediaDataStorage`](avmediadatastorage.md) object that indicates the location to which the system writes media data when it’s inserted or appended.

## See Also

- [var alternateGroupID: Int](avmovietrack/alternategroupid.md)
  A value that identifies the track as a member of a particular alternate group.
- [var mediaDecodeTimeRange: CMTimeRange](avmovietrack/mediadecodetimerange.md)
  A range of decode times for the track’s media.
- [var mediaPresentationTimeRange: CMTimeRange](avmovietrack/mediapresentationtimerange.md)
  A range of presentation times for the track’s media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovietrack/mediadatastorage)*