# removeAudioPlayer(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified audio player from the node, stopping playback.

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
func removeAudioPlayer(_ player: SCNAudioPlayer)
```

```objc
- (void) removeAudioPlayer:(SCNAudioPlayer *) player;
```

## Discussion

This method has no effect if the `player` parameter does not reference an audio player directly attached to the node.

## Parameters

- `player`: An audio player attached to the node.

## See Also

### Working with Positional Audio
- [func addAudioPlayer(SCNAudioPlayer)](./addaudioplayer%28_%29.md)
  Adds the specified auto player to the node and begins playback.
- [var audioPlayers: [SCNAudioPlayer]](./audioplayers.md)
  The audio players currently attached to the node.
- [func removeAllAudioPlayers()](./removeallaudioplayers%28%29.md)
  Removes all audio players attached to the node, stopping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/removeaudioplayer(_:))*