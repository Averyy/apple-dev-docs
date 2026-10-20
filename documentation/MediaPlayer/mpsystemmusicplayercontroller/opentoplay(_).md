# openToPlay(_:)

**Framework**: Media Player  
**Kind**: method  
**Required**: Yes

Opens the Music app and plays the designated videos.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func openToPlay(_ queueDescriptor: MPMusicPlayerQueueDescriptor)
```

#### Discussion

This method launches the user’s Music app, opens to the Now Playing screen, and begins playback of the video. If the Music app isn’t installed on the device, the system ignores this method and doesn’t play the videos.

## Parameters

- `queueDescriptor`: The queue descriptor that contains the video items to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpsystemmusicplayercontroller/opentoplay(_:))*