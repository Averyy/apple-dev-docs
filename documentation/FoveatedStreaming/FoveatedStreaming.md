# Foveated Streaming

**Framework**: Foveated Streaming  
**Kind**: module

Foveated Streaming enables visionOS apps to display high-resolution, low-latency immersive content from streaming endpoints.

**Availability**:
- visionOS 26.4+ (Beta)

#### Overview

The Foveated Streaming framework provides a session-based API for establishing connections from Apple Vision Pro to local and cloud streaming endpoints. The endpoint host streams high quality content only where necessary based on information about the approximate region where the person is looking, ensuring performance. Applications and games can integrate with the NVIDIA CloudXR™ SDK to become streaming endpoints.

On Apple Vision Pro, Foveated Streaming allows you to display visionOS spatial content alongside streaming content. For example, a flight simulator app can render a cockpit using [`RealityKit`](https://developer.apple.com/documentation/RealityKit), and stream a processor-intensive landscape from a remote computer to the device.

The core workflow involves creating a [`FoveatedStreamingSession`](foveatedstreamingsession.md), establishing a connection to the external streaming endpoint, and presenting the streamed content inside the app’s [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace). All of the features of `ImmersiveSpace` are available, including progressive and mixed immersion styles. A bidirectional message channel system allows visionOS apps to exchange custom data with streaming endpoints, allowing apps to configure the streamed content with a native [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) interface.

## Topics

### Essentials
- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)
  Integrate NVIDIA CloudXR™ and the session management connection protocol into your desktop or cloud application to stream high-fidelity spatial content to Apple Vision Pro.
- [Establishing foveated streaming sessions with Apple Vision Pro](establishing-foveated-streaming-sessions-with-apple-vision-pro.md)
  Discover, pair, and manage streaming sessions between Apple Vision Pro and local streaming endpoints by implementing the session management connection protocol.
- [Creating a foveated streaming client on visionOS](creating-a-foveated-streaming-client-on-visionos.md)
  Build a visionOS app that streams high-fidelity immersive content from a computer or the cloud using the Foveated Streaming framework.
### Classes
- [class FoveatedStreamingSession](foveatedstreamingsession.md)
  A session that manages a foveated streaming connection to a local or remote streaming endpoint.
### Structures
- [struct FoveatedStreamingSpaceContent](foveatedstreamingspacecontent.md)
  A type that defines the content of an immersive space displaying a foveated stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FoveatedStreaming)*