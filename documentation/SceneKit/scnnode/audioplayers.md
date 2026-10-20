# audioPlayers

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The audio players currently attached to the node.

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
var audioPlayers: [SCNAudioPlayer] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SCNAudioPlayer *> * audioPlayers;
```

#### Discussion

Positional audio effects from a player attached to a node are based on that node’s position relative to the [`audioListener`](../scnscenerenderer/audiolistener.md) position in the scene.

After an audio player completes playback, SceneKit automatically removes it from the node. Therefore, this array always contains audio players that are currently playing back audio.

## See Also

### Working with Positional Audio
- [func addAudioPlayer(SCNAudioPlayer)](./addaudioplayer%28_%29.md)
  Adds the specified auto player to the node and begins playback.
- [func removeAudioPlayer(SCNAudioPlayer)](./removeaudioplayer%28_%29.md)
  Removes the specified audio player from the node, stopping playback.
- [func removeAllAudioPlayers()](./removeallaudioplayers%28%29.md)
  Removes all audio players attached to the node, stopping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/audioplayers)*