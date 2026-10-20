# attachedNodes

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A read-only set that contains the nodes you attach to the audio engine.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var attachedNodes: Set<AVAudioNode> { get }
```

```objc
@property (copy, readonly) NSSet<AVAudioNode *> * attachedNodes;
```

## See Also

### Attaching and detaching audio nodes
- [func attach(AVAudioNode)](./attach%28_%29.md)
  Attaches an audio node to the audio engine.
- [func detach(AVAudioNode)](./detach%28_%29.md)
  Detaches an audio node from the audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/attachednodes)*