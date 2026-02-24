# init(foveatedStreaming:)

**Framework**: SwiftUI  
**Kind**: init

Creates an immersive space to display foveated streaming content.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
init(foveatedStreaming session: FoveatedStreamingSession) where Content == ImmersiveSpaceViewContent<FoveatedStreamingSpaceContent>, Data == Never
```

## Parameters

- `session`: The foveated streaming session whose streamed content the space displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(foveatedstreaming:))*