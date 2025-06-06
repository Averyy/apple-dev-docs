# AVMovieTrack

**Framework**: AVFoundation  
**Kind**: class

A track in a movie that conforms to the QuickTime or ISO base media file format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVMovieTrack
```

## Topics

### Retrieving Track Information
- [var alternateGroupID: Int](avmovietrack/alternategroupid.md)
  A value that identifies the track as a member of a particular alternate group.
- [var mediaDataStorage: AVMediaDataStorage?](avmovietrack/mediadatastorage.md)
  The storage container for media data added to a track.
- [var mediaDecodeTimeRange: CMTimeRange](avmovietrack/mediadecodetimerange.md)
  A range of decode times for the track’s media.
- [var mediaPresentationTimeRange: CMTimeRange](avmovietrack/mediapresentationtimerange.md)
  A range of presentation times for the track’s media.

## Relationships

### Inherits From
- [AVAssetTrack](avassettrack.md)
### Inherited By
- [AVFragmentedMovieTrack](avfragmentedmovietrack.md)
- [AVMutableMovieTrack](avmutablemovietrack.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMovie](avmovie.md)
  An object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovietrack)*