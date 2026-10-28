# isPositional

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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
var isPositional: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isPositional) BOOL positional;
```

## Discussion

If [`true`](../../Swift/true.md), the audio mixer considers the position and velocity of the [`SKAudioNode`](../skaudionode.md) relative to scene’s current [`listener`](../skscene/listener.md) node. The mixer applies distance attenuation, doppler shift, and pan effects to the sound. If [`false`](../../Swift/false.md), then the sound is played normally. The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring Audio Nodes
- [var avAudioNode: AVAudioNode?](./avaudionode.md)
  The audio node’s current audio asset.
- [var autoplayLooped: Bool](./autoplaylooped.md)
  A Boolean value that indicates whether the audio should play in a loop when the node is added to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/ispositional)*