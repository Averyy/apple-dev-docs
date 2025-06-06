# isPositional

**Framework**: SpriteKit  
**Kind**: property

A Boolean property that indicates whether the node’s audio is altered based on the position of the node.

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
@MainActor
var isPositional: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the audio mixer considers the position and velocity of the [`SKAudioNode`](skaudionode.md) relative to scene’s current [`listener`](skscene/listener.md) node. The mixer applies distance attenuation, doppler shift, and pan effects to the sound. If [`false`](https://developer.apple.com/documentation/swift/false), then the sound is played normally. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var avAudioNode: AVAudioNode?](skaudionode/avaudionode.md)
  The audio node’s current audio asset.
- [var autoplayLooped: Bool](skaudionode/autoplaylooped.md)
  A Boolean value that indicates whether the audio should play in a loop when the node is added to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/ispositional)*