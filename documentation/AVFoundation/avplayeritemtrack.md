# AVPlayerItemTrack

**Framework**: AVFoundation  
**Kind**: class

An object that represents the presentation state of an asset track during playback.

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
@MainActor
class AVPlayerItemTrack
```

## Topics

### Setting the Enabled State
- [var isEnabled: Bool](avplayeritemtrack/isenabled.md)
  A Boolean value that indicates whether the player item presents the track’s media during playback.
### Configuring Video Properties
- [var currentVideoFrameRate: Float](avplayeritemtrack/currentvideoframerate.md)
  The current frame rate of the video track as it plays.
- [var videoFieldMode: String?](avplayeritemtrack/videofieldmode.md)
  A mode that specifies the handling of video frames that contain multiple fields.
- [let AVPlayerItemTrackVideoFieldModeDeinterlaceFields: String](avplayeritemtrackvideofieldmodedeinterlacefields.md)
  A video field mode that requests deinterlacing of video fields.
### Accessing the Asset Track
- [var assetTrack: AVAssetTrack?](avplayeritemtrack/assettrack.md)
  An asset track that provides the media for the player item track.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [class AVPlayer](avplayer.md)
  An object that provides the interface to control the player’s transport behavior.
- [class AVPlayerItem](avplayeritem.md)
  An object that models the timing and presentation state of an asset during playback.
- [class AVQueuePlayer](avqueueplayer.md)
  An object that plays a sequence of player items.
- [class AVPlayerLooper](avplayerlooper.md)
  An object that loops media content using a queue player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack)*