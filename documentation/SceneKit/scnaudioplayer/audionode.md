# audioNode

**Framework**: SceneKit  
**Kind**: property

The audio node SceneKit uses for mixing audio from this player.

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
var audioNode: AVAudioNode? { get }
```

#### Discussion

SceneKit uses this [`AVAudioNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioNode) object to perform 3D positional mixing during playback. Use this object to vary parameters such as volume and reverb in real time during playback. To set default values for those parameters, use the [`audioSource`](scnaudioplayer/audiosource.md) property.

## See Also

- [var audioSource: SCNAudioSource?](scnaudioplayer/audiosource.md)
  The source of audio played by this player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/audionode)*