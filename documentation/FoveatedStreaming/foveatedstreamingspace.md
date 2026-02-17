# FoveatedStreamingSpace

**Framework**: Foveated Streaming  
**Kind**: struct

An immersive space that displays foveated streaming content.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct FoveatedStreamingSpace<Content> where Content : View
```

## Mentions

- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)

#### Overview

You can add [`RealityKit`](https://developer.apple.com/documentation/RealityKit) content to your space that coexists alongside the streamed content, for example:

```swift
FoveatedStreamingSpace(session: session) {
    RealityView { content in
        // Add a sphere to the immersive space.
        let entity = ModelEntity(mesh: .generateSphere(radius: 0.1),
                                 materials: [SimpleMaterial()])
        content.add(entity)
    }
}
```

## Topics

### Initializers
- [init(session: FoveatedStreamingSession, content: () -> Content)](foveatedstreamingspace/init(session:content:).md)
  Creates an immersive space to display foveated streaming content alongside `RealityKit` content.
### Instance Properties
- [let session: FoveatedStreamingSession](foveatedstreamingspace/session.md)
  The foveated streaming session the immersive space displays streamed content for.

## Relationships

### Conforms To
- [Scene](../SwiftUI/Scene.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class FoveatedStreamingSession](foveatedstreamingsession.md)
  A session that manages a foveated streaming connection to a local or remote streaming endpoint.
- [struct OpenFoveatedStreamingSpaceAction](openfoveatedstreamingspaceaction.md)
  An action that presents a foveated streaming space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingspace)*