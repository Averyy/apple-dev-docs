# listener

**Framework**: SpriteKit  
**Kind**: property

A node used to determine the position of the listener for positional audio in the scene.

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
weak var listener: SKNode? { get set }
```

## Mentions

- [Using Audio Nodes with the Scene’s Listener](using-audio-nodes-with-the-scene-s-listener.md)

#### Discussion

The default value is `nil`, which means that the scene’s origin is used as the listener position for audio effects played by [`SKAudioNode`](skaudionode.md) objects in the scene. If a non-`nil` value is specified, it must be a node in the scene.

Typically, you want the [`camera`](skscene/camera.md) to be the listener so that audio nodes which are on screen are louder than off screen ones. In a game, the node that defines the player would likely be set as the `listener`.

## See Also

- [Using Audio Nodes with the Scene’s Listener](using-audio-nodes-with-the-scene-s-listener.md)
  Add audio to your scene, and optionally give it 2D-positional mixing characteristics.
- [var audioEngine: AVAudioEngine](skscene/audioengine.md)
  The AVFoundation audio engine used to play audio from audio nodes contained in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/listener)*