# init(renderBlock:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio source node with a block that supplies audio data.

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
init(renderBlock block: @escaping AVAudioSourceNodeRenderBlock)
```

#### Discussion

When connecting the audio source node to another node, the system uses the connection format to set the audio format for the output bus.

Depending on the audio engine’s operating mode, call the block on real-time or nonreal-time threads. When rendering to a device, avoid making blocking calls within the block.

The system sets the node’s output format using the audio format for the render block. When reconnecting the node with a different output format, the audio format for the block changes.

## Parameters

- `block`: The block to supply audio data to the output.

## See Also

- [typealias AVAudioSourceNodeRenderBlock](avaudiosourcenoderenderblock.md)
  A block that supplies audio data to an audio source node.
- [init(format: AVAudioFormat, renderBlock: AVAudioSourceNodeRenderBlock)](avaudiosourcenode/init(format:renderblock:).md)
  Creates an audio source node with the audio format and a block that supplies audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosourcenode/init(renderblock:))*