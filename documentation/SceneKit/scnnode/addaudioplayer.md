# addAudioPlayer(_:)

**Framework**: SceneKit  
**Kind**: method

Adds the specified auto player to the node and begins playback.

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
func addAudioPlayer(_ player: SCNAudioPlayer)
```

#### Discussion

Positional audio effects from a player attached to a node are based on that node’s position relative to the [`audioListener`](scnscenerenderer/audiolistener.md) position in the scene.

After playback has completed, SceneKit automatically removes the audio player from the node.

## Parameters

- `player`: An audio player object.

## See Also

- [var audioPlayers: [SCNAudioPlayer]](scnnode/audioplayers.md)
  The audio players currently attached to the node.
- [func removeAudioPlayer(SCNAudioPlayer)](scnnode/removeaudioplayer(_:).md)
  Removes the specified audio player from the node, stopping playback.
- [func removeAllAudioPlayers()](scnnode/removeallaudioplayers.md)
  Removes all audio players attached to the node, stopping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/addaudioplayer(_:))*