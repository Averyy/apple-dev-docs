# audioEngine

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The audio engine SceneKit uses for playing scene sounds.

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
var audioEngine: AVAudioEngine { get }
```

#### Discussion

SceneKit uses this audio engine to play sounds from [`SCNAudioPlayer`](scnaudioplayer.md) objects attached to nodes in the scene. You can use this object directly to add other sound sources not related to scene contents, or to add other sound processing nodes or mixing nodes to the audio engine. To identify the node SceneKit uses for spatializing scene sounds when connecting other nodes, use the [`audioEnvironmentNode`](scnscenerenderer/audioenvironmentnode.md) property.

## See Also

- [var audioListener: SCNNode?](scnscenerenderer/audiolistener.md)
  The node representing the listener’s position in the scene for use with positional audio effects.
- [var audioEnvironmentNode: AVAudioEnvironmentNode](scnscenerenderer/audioenvironmentnode.md)
  The 3D audio mixing node SceneKit uses for positional audio effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/audioengine)*