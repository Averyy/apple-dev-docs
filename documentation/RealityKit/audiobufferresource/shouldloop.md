# shouldLoop

**Framework**: RealityKit  
**Kind**: property

Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var shouldLoop: Bool { get }
```

## See Also

- [init(buffer: AVAudioBuffer, inputMode: AudioResource.InputMode, shouldLoop: Bool) throws](audiobufferresource/init(buffer:inputmode:shouldloop:).md)
  Init an AudioBufferResource from an `AVAudioBuffer` instead of a file location. This is intended for use with `AVSpeechSynthesisVoice`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiobufferresource/shouldloop)*