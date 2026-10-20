# init(avAudioNode:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes an audio node from an AVFoundation audio node.

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
init(avAudioNode node: AVAudioNode?)
```

```objc
- (instancetype) initWithAVAudioNode:(AVAudioNode *) node;
```

#### Return Value

A newly initialized audio node.

## Parameters

- `node`: An [`AVAudioNode`](../../AVFAudio/avaudionode.md) object that holds an [`AVAudioEngine`](../../AVFAudio/avaudioengine.md) sound graph from a single sound source or URL.

## See Also

### Initializing Audio Nodes
- [convenience init(fileNamed: String)](./init%28filenamed%29.md)
  Initializes an audio node from an audio asset with the specified filename.
- [convenience init(url: URL)](./init%28url%29-8v3q0.md)
  Initializes an audio node from an audio asset with the specified URL.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to initialize an audio node that has been unarchived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/init(avaudionode:)-969st)*