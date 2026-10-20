# audioEngine

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The audio engine SceneKit uses for playing scene sounds.

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
var audioEngine: AVAudioEngine { get }
```

```objc
@property (nonatomic, readonly) AVAudioEngine * audioEngine;
```

#### Discussion

SceneKit uses this audio engine to play sounds from [`SCNAudioPlayer`](../scnaudioplayer.md) objects attached to nodes in the scene. You can use this object directly to add other sound sources not related to scene contents, or to add other sound processing nodes or mixing nodes to the audio engine. To identify the node SceneKit uses for spatializing scene sounds when connecting other nodes, use the [`audioEnvironmentNode`](./audioenvironmentnode.md) property.

## See Also

### Working With Positional Audio
- [var audioListener: SCNNode?](./audiolistener.md)
  The node representing the listener’s position in the scene for use with positional audio effects.
- [var audioEnvironmentNode: AVAudioEnvironmentNode](./audioenvironmentnode.md)
  The 3D audio mixing node SceneKit uses for positional audio effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/audioengine)*