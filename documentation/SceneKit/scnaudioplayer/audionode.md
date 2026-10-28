# audioNode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The audio node SceneKit uses for mixing audio from this player.

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
var audioNode: AVAudioNode? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVAudioNode * audioNode;
```

## Discussion

SceneKit uses this [`AVAudioNode`](../../AVFAudio/avaudionode.md) object to perform 3D positional mixing during playback. Use this object to vary parameters such as volume and reverb in real time during playback. To set default values for those parameters, use the [`audioSource`](./audiosource.md) property.

## See Also

### Working with Audio Sources
- [var audioSource: SCNAudioSource?](./audiosource.md)
  The source of audio played by this player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/audionode)*