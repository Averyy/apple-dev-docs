# autoplayLooped

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the audio should play in a loop when the node is added to the scene.

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
var autoplayLooped: Bool { get set }
```

#### Discussion

If the property value is [`true`](https://developer.apple.com/documentation/Swift/true), then the audio starts playing as soon as the node is added to the scene, and repeats after it completes. If [`false`](https://developer.apple.com/documentation/Swift/false), then the audio node’s content never plays automatically. It must be explicitly scheduled using the scene’s audio engine. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var avAudioNode: AVAudioNode?](skaudionode/avaudionode.md)
  The audio node’s current audio asset.
- [var isPositional: Bool](skaudionode/ispositional.md)
  A Boolean property that indicates whether the node’s audio is altered based on the position of the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/autoplaylooped)*