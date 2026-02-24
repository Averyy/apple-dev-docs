# init(foveatedStreaming:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an immersive space to display foveated streaming content alongside `RealityKit` content.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
init<V>(foveatedStreaming session: FoveatedStreamingSession, @ViewBuilder content: @escaping () -> V) where Content == ImmersiveSpaceViewContent<FoveatedStreamingSpaceContent>, Data == Never, V : View
```

#### Discussion

You can add [`RealityKit`](https://developer.apple.com/documentation/RealityKit) content to your space that coexists alongside the streamed content, for example:

```swift
ImmersiveSpace(foveatedStreaming: session) {
    RealityView { content in
        // Add a sphere to the immersive space.
        let entity = ModelEntity(mesh: .generateSphere(radius: 0.1),
                         materials: [SimpleMaterial()])
        content.add(entity)
    }
}
```

## Parameters

- `session`: The foveated streaming session whose streamed content the space displays.
- `content`: An immersive space content builder that defines the content of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(foveatedstreaming:content:))*