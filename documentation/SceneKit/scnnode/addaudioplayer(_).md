# addAudioPlayer(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified auto player to the node and begins playback.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func addAudioPlayer(_ player: SCNAudioPlayer)
```

```objc
- (void) addAudioPlayer:(SCNAudioPlayer *) player;
```

#### Discussion

Positional audio effects from a player attached to a node are based on that node’s position relative to the [`audioListener`](../scnscenerenderer/audiolistener.md) position in the scene.

After playback has completed, SceneKit automatically removes the audio player from the node.

## Parameters

- `player`: An audio player object.

## See Also

### Working with Positional Audio
- [var audioPlayers: [SCNAudioPlayer]](./audioplayers.md)
  The audio players currently attached to the node.
- [func removeAudioPlayer(SCNAudioPlayer)](./removeaudioplayer%28_%29.md)
  Removes the specified audio player from the node, stopping playback.
- [func removeAllAudioPlayers()](./removeallaudioplayers%28%29.md)
  Removes all audio players attached to the node, stopping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/addaudioplayer(_:))*