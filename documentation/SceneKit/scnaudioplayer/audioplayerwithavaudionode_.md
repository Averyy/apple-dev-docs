# audioPlayerWithAVAudioNode:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Returns an audio player (creating one if necessary) to play an audio node.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) audioPlayerWithAVAudioNode:(AVAudioNode *) audioNode;
```

#### Return Value

A positional audio player object.

#### Discussion

Creating an audio player from an audio node does not attach that node to an [`AVAudioEngine`](../../AVFAudio/avaudioengine.md) object for mixing and playback—instead, this option allows you to build your own audio node graph for custom effects before manually adding it to the [`audioEngine`](../scnscenerenderer/audioengine.md) object of the view (or other SceneKit renderer) displaying the scene. Then, after you attach the audio player to an [`SCNNode`](../scnnode.md) object, SceneKit continually updates the audio node’s 3D mixing parameters to match the position of the scene node.

When you use this method, SceneKit creates an audio player for the specified [`AVAudioNode`](../../AVFAudio/avaudionode.md) object or, if an audio player for that node already exists and is not in use, SceneKit reuses the existing player object.

## Parameters

- `audioNode`: An audio node object.

## See Also

### Creating an Audio Player
- [init(source: SCNAudioSource)](./init%28source%29.md)
  Initializes an audio player for playing the specified simple audio source.
- [init(avAudioNode: AVAudioNode)](./init%28avaudionode%29-4u514.md)
  Initializes an audio player for playing the specified AVFoundation audio node.
- [+ audioPlayerWithSource:](./audioplayerwithsource_.md)
  Returns an audio player (creating one if necessary) to play a simple audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/audioplayerwithavaudionode:)*