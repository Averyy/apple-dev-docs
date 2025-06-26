# init(buffer:inputMode:shouldLoop:)

**Framework**: RealityKit  
**Kind**: init

Init an AudioBufferResource from an `AVAudioBuffer` instead of a file location. This is intended for use with `AVSpeechSynthesisVoice`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@MainActor
@preconcurrency init(buffer: AVAudioBuffer, inputMode: AudioResource.InputMode = .spatial, shouldLoop: Bool = false) throws
```

#### Discussion

> **Note**: This function throws an error when the `AVAudioBuffer`  cannot be cast or converted to `AVAudioPCMBuffer`.

## Parameters

- `inputMode`: How the audio engine processes a resource. nonSpatial, spatial, ambient
- `shouldLoop`: Bool value to decide if the audio clip should loop

## See Also

- [var shouldLoop: Bool](audiobufferresource/shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiobufferresource/init(buffer:inputmode:shouldloop:))*