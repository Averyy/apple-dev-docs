# audioEngine

**Framework**: SpriteKit  
**Kind**: property

The AVFoundation audio engine used to play audio from audio nodes contained in the scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var audioEngine: AVAudioEngine { get }
```

#### Discussion

An audio engine instance is automatically created for you when the scene is created. You can use methods and properties on a scene’s audio engine for overall control of all of its child audio nodes. The following code shows how a scene’s overall volume can be reduced from its default of 1.0 down to 0.2 and then paused:

```swift
let scene = SKScene()
scene.audioEngine.mainMixerNode.outputVolume = 0.2
scene.audioEngine.pause()
```

## See Also

- [Using Audio Nodes with the Scene’s Listener](using-audio-nodes-with-the-scene-s-listener.md)
  Add audio to your scene, and optionally give it 2D-positional mixing characteristics.
- [var listener: SKNode?](skscene/listener.md)
  A node used to determine the position of the listener for positional audio in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/audioengine)*