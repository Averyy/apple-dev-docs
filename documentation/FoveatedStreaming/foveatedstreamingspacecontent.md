# FoveatedStreamingSpaceContent

**Framework**: Foveated Streaming  
**Kind**: struct

A type that defines the content of an immersive space displaying a foveated stream.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency struct FoveatedStreamingSpaceContent
```

#### Overview

Don’t use `FoveatedStreamingSpaceContent` directly. The Foveated Streaming framework uses it when you call [`init(foveatedStreaming:content:)`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace/init(foveatedStreaming:content:)) to display spatial content from a foveated streaming session alongside [`RealityKit`](https://developer.apple.com/documentation/RealityKit) content:

```swift
ImmersiveSpace(foveatedStreaming: session) {
    RealityView { content in
        // Optional: Add `RealityKit` content to the immersive space to co-exist with the streamed content.
    }
}
```

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingspacecontent)*