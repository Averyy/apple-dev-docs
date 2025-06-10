# playbackCoordinationMedium

**Framework**: AVFoundation  
**Kind**: property

The AVPlaybackCoordinationMedium this playback coordinator is connected to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var playbackCoordinationMedium: AVPlaybackCoordinationMedium? { get }
```

#### Discussion

This is the AVPlaybackCoordinationMedium the playback coordinator is connected to. If not NULL, the playback coordinator is connected to the specified coordination medium. The playback coordinator is not available to coordinate with a group session. If NULL, the playback coordinator is not connected to any playback coordination medium. The playback coordinator is available to coordinate with a group session through the `coordinateWithSession` API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator/playbackcoordinationmedium)*