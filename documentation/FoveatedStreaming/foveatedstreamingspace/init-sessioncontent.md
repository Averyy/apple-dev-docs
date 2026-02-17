# init(session:content:)

**Framework**: Foveated Streaming  
**Kind**: init

Creates an immersive space to display foveated streaming content alongside `RealityKit` content.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(session: FoveatedStreamingSession, @ViewBuilder content: @escaping () -> Content)
```

## Parameters

- `session`: The foveated streaming session whose streamed content the space displays.
- `content`: An immersive space content builder that defines the content of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingspace/init(session:content:))*