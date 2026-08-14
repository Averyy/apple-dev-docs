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

Don’t use `FoveatedStreamingSpaceContent` directly. The Foveated Streaming framework uses it when you call [`init(foveatedStreaming:content:)`](https://developer.apple.com/documentation/swiftui/immersivespace/init(foveatedstreaming:content:)) to display spatial content from a foveated streaming session alongside [`RealityKit`](https://developer.apple.com/documentation/realitykit) content:

```swift
ImmersiveSpace(foveatedStreaming: session) {
    RealityView { content in
        // Optional: Add `RealityKit` content to the immersive space to co-exist with the streamed content.
    }
}
```

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)

## See Also

- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)
  Integrate NVIDIA CloudXR™ and the session management connection protocol into your desktop or cloud application to stream high-fidelity spatial content to Apple Vision Pro.
- [Establishing foveated streaming sessions with Apple Vision Pro](establishing-foveated-streaming-sessions-with-apple-vision-pro.md)
  Discover, pair, and manage streaming sessions between Apple Vision Pro and local streaming endpoints by implementing the session management connection protocol.
- [Creating a foveated streaming client on visionOS](creating-a-foveated-streaming-client-on-visionos.md)
  Build a visionOS app that streams high-fidelity immersive content from a computer or the cloud using the Foveated Streaming framework.
- [Analyzing the performance of a foveated streaming session](analyzing-the-performance-of-a-foveated-streaming-session.md)
  Use the Foveated Streaming Statistics instrument to evaluate the performance of your visionOS streaming client app.
- [class FoveatedStreamingSession](foveatedstreamingsession.md)
  A session that manages a foveated streaming connection to a local or remote streaming endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingspacecontent)*