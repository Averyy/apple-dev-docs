# audioEnvironmentNode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The 3D audio mixing node SceneKit uses for positional audio effects.

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
var audioEnvironmentNode: AVAudioEnvironmentNode { get }
```

```objc
@property (nonatomic, readonly) AVAudioEnvironmentNode * audioEnvironmentNode;
```

## Discussion

SceneKit uses this audio node to spatialize sounds from [`SCNAudioPlayer`](../scnaudioplayer.md) objects attached to nodes in the scene. You can use this object in conjunction with the [`audioEngine`](./audioengine.md) property to rearrange the audio graph to add other, non-spatialized audio sources or mix in audio processing effects.

## See Also

### Working With Positional Audio
- [var audioListener: SCNNode?](./audiolistener.md)
  The node representing the listener’s position in the scene for use with positional audio effects.
- [var audioEngine: AVAudioEngine](./audioengine.md)
  The audio engine SceneKit uses for playing scene sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/audioenvironmentnode)*