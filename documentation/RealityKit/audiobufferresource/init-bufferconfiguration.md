# init(buffer:configuration:)

**Framework**: RealityKit  
**Kind**: init

Creates an `AudioBufferResource` with the given `AVAudioBuffer` and configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init(buffer: AVAudioBuffer, configuration: AudioBufferResource.Configuration = .init()) throws
```

#### Discussion

> **Note**: An error if the given `buffer` is not or cannot be converted to a non-interleaved PCM buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiobufferresource/init(buffer:configuration:))*