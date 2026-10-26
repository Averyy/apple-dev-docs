# init(avAudioNode:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Initializes an audio player for playing the specified AVFoundation audio node.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
init(avAudioNode audioNode: AVAudioNode)
```

```objc
- (instancetype) initWithAVAudioNode:(AVAudioNode *) audioNode;
```

#### Return Value

A positional audio player object.

#### Discussion

Using this initializer is typically not necessary. Instead, call the [`audioPlayerWithAVAudioNode:`](./audioplayerwithavaudionode_.md) method, which returns a cached audio player object if one for the specified [`AVAudioNode`](../../AVFAudio/avaudionode.md) object has already been created and is available for use.

## Parameters

- `audioNode`: An audio node object.

## See Also

### Creating an Audio Player
- [init(source: SCNAudioSource)](./init%28source%29.md)
  Initializes an audio player for playing the specified simple audio source.
- [+ audioPlayerWithSource:](./audioplayerwithsource_.md)
  Returns an audio player (creating one if necessary) to play a simple audio source.
- [+ audioPlayerWithAVAudioNode:](./audioplayerwithavaudionode_.md)
  Returns an audio player (creating one if necessary) to play an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/init(avaudionode:)-4u514)*