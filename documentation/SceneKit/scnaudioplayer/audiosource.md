# audioSource

**Framework**: SceneKit  
**Kind**: property

The source of audio played by this player.

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
var audioSource: SCNAudioSource? { get }
```

#### Discussion

An [`SCNAudioSource`](scnaudiosource.md) object represents a distinct source of audio—for example, a sound file—that can be reused and shared by many player objects. Use a player’s audio source to configure the default values for playback parameters such as volume and reverb. To vary those parameters in real time during playback, use the [`audioNode`](scnaudioplayer/audionode.md) property to work with the underlying [`AVAudioNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioNode) object.

If the player was created with the [`audioPlayerWithAVAudioNode:`](scnaudioplayer/audioplayerwithavaudionode:.md) method, this property’s value is `nil`.

## See Also

- [var audioNode: AVAudioNode?](scnaudioplayer/audionode.md)
  The audio node SceneKit uses for mixing audio from this player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/audiosource)*