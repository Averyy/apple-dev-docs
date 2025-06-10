# init(avAudioNode:)

**Framework**: SceneKit  
**Kind**: init

Initializes an audio player for playing the specified AVFoundation audio node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(avAudioNode audioNode: AVAudioNode)
```

#### Return Value

A positional audio player object.

#### Discussion

Using this initializer is typically not necessary. Instead, call the [`audioPlayerWithAVAudioNode:`](scnaudioplayer/audioplayerwithavaudionode:.md) method, which returns a cached audio player object if one for the specified [`AVAudioNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioNode) object has already been created and is available for use.

## Parameters

- `audioNode`: An audio node object.

## See Also

- [init(source: SCNAudioSource)](scnaudioplayer/init(source:).md)
  Initializes an audio player for playing the specified simple audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/init(avaudionode:))*