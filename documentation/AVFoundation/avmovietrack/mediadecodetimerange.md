# mediaDecodeTimeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A range of decode times for the track’s media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mediaDecodeTimeRange: CMTimeRange { get }
```

```objc
@property (nonatomic, readonly) CMTimeRange mediaDecodeTimeRange;
```

## See Also

### Retrieving track information
- [var alternateGroupID: Int](./alternategroupid.md)
  A value that identifies the track as a member of a particular alternate group.
- [var mediaDataStorage: AVMediaDataStorage?](./mediadatastorage.md)
  The storage container for media data added to a track.
- [var mediaPresentationTimeRange: CMTimeRange](./mediapresentationtimerange.md)
  A range of presentation times for the track’s media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovietrack/mediadecodetimerange)*