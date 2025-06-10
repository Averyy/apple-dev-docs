# avAudioNode

**Framework**: SpriteKit  
**Kind**: property

The audio node’s current audio asset.

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
var avAudioNode: AVAudioNode? { get set }
```

#### Discussion

The AV audio node must refer to an [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) sound graph from a single sound source or URL.

## See Also

- [var isPositional: Bool](skaudionode/ispositional.md)
  A Boolean property that indicates whether the node’s audio is altered based on the position of the node.
- [var autoplayLooped: Bool](skaudionode/autoplaylooped.md)
  A Boolean value that indicates whether the audio should play in a loop when the node is added to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/avaudionode)*