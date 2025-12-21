# playbackCoordinationMedium

**Framework**: AVFoundation  
**Kind**: property

The AVPlaybackCoordinationMedium this playback coordinator is connected to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var playbackCoordinationMedium: AVPlaybackCoordinationMedium? { get }
```

#### Discussion

This is the AVPlaybackCoordinationMedium the playback coordinator is connected to. If not NULL, the playback coordinator is connected to the specified coordination medium. The playback coordinator is not available to coordinate with a group session. If NULL, the playback coordinator is not connected to any playback coordination medium. The playback coordinator is available to coordinate with a group session through the `coordinateWithSession` API.

## See Also

- [func coordinate(using: AVPlaybackCoordinationMedium?) throws](avplayerplaybackcoordinator/coordinate(using:).md)
  Connects the playback coordinator to the coordination medium


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator/playbackcoordinationmedium)*