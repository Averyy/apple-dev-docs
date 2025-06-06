# Using Audio Nodes with the Scene’s Listener

**Framework**: SpriteKit

Add audio to your scene, and optionally give it 2D-positional mixing characteristics.

#### Overview

The simplest way to add audio to a SpriteKit scene is to add a child [`SKAudioNode`](skaudionode.md) to it:

```swift
let audio = SKAudioNode(fileNamed: "drums.mp3")

spriteKitViewController.scene.addChild(audio)

```

However, if you define the presented scene’s [`listener`](skscene/listener.md), its audio nodes are played back with positional sound mixing. For example, if you set the scene’s `listener` to be the scene’s `camera` and then add audio nodes as children to various parent nodes in the scene, the further away the parent nodes are from the center of the screen, the quieter their audio will be played.

## See Also

- [var listener: SKNode?](skscene/listener.md)
  A node used to determine the position of the listener for positional audio in the scene.
- [var audioEngine: AVAudioEngine](skscene/audioengine.md)
  The AVFoundation audio engine used to play audio from audio nodes contained in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/using-audio-nodes-with-the-scene-s-listener)*