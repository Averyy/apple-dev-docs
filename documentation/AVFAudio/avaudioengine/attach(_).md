# attach(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Attaches an audio node to the audio engine.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func attach(_ node: AVAudioNode)
```

```objc
- (void) attachNode:(AVAudioNode *) node;
```

## Discussion

An instance of [`AVAudioNode`](../avaudionode.md) isn’t usable until you attach it to the audio engine using this method.

```swift
// Create a player node that's used for audio playback.
let playerNode = AVAudioPlayerNode()

// Attach the player node to the engine.
engine.attach(playerNode)
```

## Parameters

- `node`: The audio node to attach.

## See Also

### Attaching and detaching audio nodes
- [func detach(AVAudioNode)](./detach%28_%29.md)
  Detaches an audio node from the audio engine.
- [var attachedNodes: Set<AVAudioNode>](./attachednodes.md)
  A read-only set that contains the nodes you attach to the audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/attach(_:))*