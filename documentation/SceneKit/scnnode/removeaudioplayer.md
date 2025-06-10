# removeAudioPlayer(_:)

**Framework**: SceneKit  
**Kind**: method

Removes the specified audio player from the node, stopping playback.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removeAudioPlayer(_ player: SCNAudioPlayer)
```

#### Discussion

This method has no effect if the `player` parameter does not reference an audio player directly attached to the node.

## Parameters

- `player`: An audio player attached to the node.

## See Also

- [func addAudioPlayer(SCNAudioPlayer)](scnnode/addaudioplayer(_:).md)
  Adds the specified auto player to the node and begins playback.
- [var audioPlayers: [SCNAudioPlayer]](scnnode/audioplayers.md)
  The audio players currently attached to the node.
- [func removeAllAudioPlayers()](scnnode/removeallaudioplayers.md)
  Removes all audio players attached to the node, stopping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/removeaudioplayer(_:))*