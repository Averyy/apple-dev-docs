# shouldLoop

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use AudioBufferResource.init(buffer:configuration:) instead.

## Declaration

```swift
@MainActor
@preconcurrency var shouldLoop: Bool { get }
```

## See Also

### Deprecated
- [init(buffer: AVAudioBuffer, inputMode: AudioResource.InputMode, shouldLoop: Bool) throws](./init%28buffer,inputmode,shouldloop%29.md)
  Init an AudioBufferResource from an `AVAudioBuffer` instead of a file location. This is intended for use with `AVSpeechSynthesisVoice`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiobufferresource/shouldloop)*