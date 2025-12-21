# Audio.GeneratorRenderHandler

**Framework**: RealityKit  
**Kind**: typealias

A handler that generates real-time audio.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
typealias GeneratorRenderHandler = AVAudioSourceNodeRenderBlock
```

#### Discussion

The audio format is `Float32` with a sample rate of `48000`.

> **Note**: The system executes your handler in a real-time audio thread. Achieve optimal performance by ensuring the closure finishes quickly. Avoid heap allocations or locks within the closure.

> **Note**: As of Swift 6, you should mark your handler as @Sendable to ensure no actor isolation is inferred and that any captured values are safe to use from a realtime audio concurrency domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/generatorrenderhandler)*