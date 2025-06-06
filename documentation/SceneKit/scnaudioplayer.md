# SCNAudioPlayer

**Framework**: SceneKit  
**Kind**: class

A controller for playback of a positional audio source in a SceneKit scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SCNAudioPlayer
```

#### Overview

An [`SCNAudioPlayer`](scnaudioplayer.md) object controls playback of a positional audio source in a SceneKit scene. To use positional audio, first create a reusable [`SCNAudioSource`](scnaudiosource.md) or [`AVAudioNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioNode) object to provide an audio stream. Then, create an audio player to control the playback of that audio source. Finally, attach the audio player to an [`SCNNode`](scnnode.md) object for spatialized 3D audio playback based on the position of that node relative to the scene’s [`audioListener`](scnscenerenderer/audiolistener.md) node.

## Topics

### Creating an Audio Player
- [init(source: SCNAudioSource)](scnaudioplayer/init(source:).md)
  Initializes an audio player for playing the specified simple audio source.
- [init(avAudioNode: AVAudioNode)](scnaudioplayer/init(avaudionode:).md)
  Initializes an audio player for playing the specified AVFoundation audio node.
### Working with Audio Sources
- [var audioSource: SCNAudioSource?](scnaudioplayer/audiosource.md)
  The source of audio played by this player.
- [var audioNode: AVAudioNode?](scnaudioplayer/audionode.md)
  The audio node SceneKit uses for mixing audio from this player.
### Responding to Playback
- [var willStartPlayback: (() -> Void)?](scnaudioplayer/willstartplayback.md)
  A block called by SceneKit when playback of the player’s audio source is about to begin.
- [var didFinishPlayback: (() -> Void)?](scnaudioplayer/didfinishplayback.md)
  A block called by SceneKit when playback of the player’s audio source has completed.

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

## See Also

- [class SCNAudioSource](scnaudiosource.md)
  A simple, reusable audio source—music or sound effects loaded from a file—for use in positional audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer)*