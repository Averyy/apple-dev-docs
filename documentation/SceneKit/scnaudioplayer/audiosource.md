# audioSource

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The source of audio played by this player.

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
var audioSource: SCNAudioSource? { get }
```

```objc
@property (nonatomic, readonly, nullable) SCNAudioSource * audioSource;
```

#### Discussion

An [`SCNAudioSource`](../scnaudiosource.md) object represents a distinct source of audio—for example, a sound file—that can be reused and shared by many player objects. Use a player’s audio source to configure the default values for playback parameters such as volume and reverb. To vary those parameters in real time during playback, use the [`audioNode`](./audionode.md) property to work with the underlying [`AVAudioNode`](../../AVFAudio/avaudionode.md) object.

If the player was created with the [`audioPlayerWithAVAudioNode:`](./audioplayerwithavaudionode_.md) method, this property’s value is `nil`.

## See Also

### Working with Audio Sources
- [var audioNode: AVAudioNode?](./audionode.md)
  The audio node SceneKit uses for mixing audio from this player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/audiosource)*