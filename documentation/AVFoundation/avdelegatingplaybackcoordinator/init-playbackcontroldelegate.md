# init(playbackControlDelegate:)

**Framework**: AVFoundation  
**Kind**: init

Creates a playback coordinator for a custom playback object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(playbackControlDelegate: any AVPlaybackCoordinatorPlaybackControlDelegate)
```

#### Discussion

If your app doesn’t use [`AVPlayer`](avplayer.md) for playback, create an instance of this class to coordinate playback of your customer player.

## Parameters

- `playbackControlDelegate`: The playback control delegate for the playback coordinator.

## See Also

- [protocol AVPlaybackCoordinatorPlaybackControlDelegate](avplaybackcoordinatorplaybackcontroldelegate.md)
  A protocol that defines the method to implement to respond to playback commands from the playback coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/init(playbackcontroldelegate:))*