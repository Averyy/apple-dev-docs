# detach(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Detaches an audio node from the audio engine.

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
func detach(_ node: AVAudioNode)
```

```objc
- (void) detachNode:(AVAudioNode *) node;
```

#### Discussion

If necessary, the audio engine safely disconnects the audio node before detaching it.

## Parameters

- `node`: The audio node to detach.

## See Also

### Attaching and detaching audio nodes
- [func attach(AVAudioNode)](./attach%28_%29.md)
  Attaches an audio node to the audio engine.
- [var attachedNodes: Set<AVAudioNode>](./attachednodes.md)
  A read-only set that contains the nodes you attach to the audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/detach(_:))*