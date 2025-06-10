# audioEnvironmentNode

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The 3D audio mixing node SceneKit uses for positional audio effects.

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
var audioEnvironmentNode: AVAudioEnvironmentNode { get }
```

#### Discussion

SceneKit uses this audio node to spatialize sounds from [`SCNAudioPlayer`](scnaudioplayer.md) objects attached to nodes in the scene. You can use this object in conjunction with the [`audioEngine`](scnscenerenderer/audioengine.md) property to rearrange the audio graph to add other, non-spatialized audio sources or mix in audio processing effects.

## See Also

- [var audioListener: SCNNode?](scnscenerenderer/audiolistener.md)
  The node representing the listener’s position in the scene for use with positional audio effects.
- [var audioEngine: AVAudioEngine](scnscenerenderer/audioengine.md)
  The audio engine SceneKit uses for playing scene sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/audioenvironmentnode)*