# SCNAudioPlayer

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A controller for playback of a positional audio source in a SceneKit scene.

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
class SCNAudioPlayer
```

```objc
@interface SCNAudioPlayer : NSObject
```

## Overview

An [`SCNAudioPlayer`](./scnaudioplayer.md) object controls playback of a positional audio source in a SceneKit scene. To use positional audio, first create a reusable [`SCNAudioSource`](./scnaudiosource.md) or [`AVAudioNode`](../AVFAudio/avaudionode.md) object to provide an audio stream. Then, create an audio player to control the playback of that audio source. Finally, attach the audio player to an [`SCNNode`](./scnnode.md) object for spatialized 3D audio playback based on the position of that node relative to the scene’s [`audioListener`](./scnscenerenderer/audiolistener.md) node.

## Topics

### Creating an Audio Player
- [init(source: SCNAudioSource)](./scnaudioplayer/init%28source%29.md)
  Initializes an audio player for playing the specified simple audio source.
- [init(avAudioNode: AVAudioNode)](./scnaudioplayer/init%28avaudionode%29-4u514.md)
  Initializes an audio player for playing the specified AVFoundation audio node.
- [+ audioPlayerWithSource:](./scnaudioplayer/audioplayerwithsource_.md)
  Returns an audio player (creating one if necessary) to play a simple audio source.
- [+ audioPlayerWithAVAudioNode:](./scnaudioplayer/audioplayerwithavaudionode_.md)
  Returns an audio player (creating one if necessary) to play an audio node.
### Working with Audio Sources
- [var audioSource: SCNAudioSource?](./scnaudioplayer/audiosource.md)
  The source of audio played by this player.
- [var audioNode: AVAudioNode?](./scnaudioplayer/audionode.md)
  The audio node SceneKit uses for mixing audio from this player.
### Responding to Playback
- [var willStartPlayback: (() -> Void)?](./scnaudioplayer/willstartplayback.md)
  A block called by SceneKit when playback of the player’s audio source is about to begin.
- [var didFinishPlayback: (() -> Void)?](./scnaudioplayer/didfinishplayback.md)
  A block called by SceneKit when playback of the player’s audio source has completed.
### Initializers
- [convenience init(AVAudioNode: AVAudioNode)](./scnaudioplayer/init%28avaudionode%29-1xsj6.md)
- [init(AVAudioNode: AVAudioNode)](./scnaudioplayer/init%28avaudionode%29-6dktc.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Audio
- [class SCNAudioSource](./scnaudiosource.md)
  A simple, reusable audio source—music or sound effects loaded from a file—for use in positional audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer)*