# Streaming a CloudXR application to Apple Vision Pro with foveation

**Framework**: Foveated Streaming

Integrate NVIDIA CloudXR™ and the streaming manager protocol into your desktop or cloud application to stream high-fidelity spatial content to Apple Vision Pro.

#### Overview

If you have an existing virtual reality game, experience, or application built for desktop computers or a cloud server, you can stream it to Apple Vision Pro with the Foveated Streaming framework.

Foveated Streaming allows your endpoint to stream high quality content only where necessary based on information about the approximate region where the person is looking, ensuring performance. On Apple Vision Pro, you can also layer native spatial content over the streamed content. For example, a racing game can render the gauges in the interior of the car with [`RealityKit`](https://developer.apple.com/documentation/RealityKit), and stream the processor-intensive outdoor environment from a remote computer to the device.

To enable streaming, integrate the following three components:

-  Download the OpenXR-compliant runtime from NVIDIA and integrate it into your streaming application.
-  When streaming from a local device, implement a protocol to handle device discovery, authentication, and session state management between your streaming application and Apple Vision Pro.
-  Build a visionOS app that connects to your streaming application, displays the streamed content in an immersive space, and enables people to interact with both the streamed content and `RealityKit` elements.

#### Add the Cloudxr Runtime to Your Application

Download the [`CloudXR SDK`](https://developer.apple.comhttps://catalog.ngc.nvidia.com/orgs/nvidia/collections/cloudxr-sdk), then follow the steps in the [`NVIDIA CloudXR SDK`](https://developer.apple.comhttps://docs.nvidia.com/cloudxr-sdk) documentation to integrate it into your app.

For an example implementation, see the [`StreamingSession-OpenXRSample`](https://developer.apple.comhttps://github.com/apple/StreamingSession/tree/main/StreamingSession-OpenXRSample/).

#### Implement the Streaming Manager Protocol

Make your streaming application discoverable to Apple Vision Pro by broadcasting a Bonjour service with the following name:

`_apple-foveated-streaming._tcp`

Add a TXT record to the Bonjour service with an entry that specifies the bundle ID of the visionOS app you’re streaming to:

| Key | Value |
| --- | --- |
| `Application-Identifier` | The bundle ID of the visionOS app. |

After discovering the streaming endpoint, Apple Vision Pro sends and expects replies to a series of Transmission Control Protocol (TCP) messages. The order of these messages is as follows:

1. Apple Vision Pro sends a `RequestConnection` message. - Your streaming application replies with an `AcknowledgeConnection` message.
2. Apple Vision Pro sends a `RequestBarcodePresentation` message. - Your streaming application presents a QR code with pairing information and replies with `AcknowledgeBarcodePresentation`.
3. After launching the CloudXR server, your streaming application sends a `MediaStreamIsReady` to the server to indicate that it’s ready to stream content.
4. Apple Vision Pro sends `SessionStatusDidChange` messages when the foveated streaming session state changes.
5. Your streaming application sends a `RequestSessionDisconnect` message to end the session.

For more information on the format and content of these messages, see [`Establishing foveated streaming sessions with Apple Vision Pro`](establishing-foveated-streaming-sessions-with-apple-vision-pro.md). For an example implementation, see the [`StreamingSession-WindowsApp`](https://developer.apple.comhttps://github.com/apple/StreamingSession/tree/main/StreamingSession-WindowsApp/).

#### Create a Visionos App

Display streamed content by building a visionOS app with the Foveated Streaming framework that does the following:

- Initializes a [`FoveatedStreamingSession`](foveatedstreamingsession.md).
- Connects to a `FoveatedStreamingSession.Endpoint`.
- Presents the streamed content in a [`FoveatedStreamingSpace`](foveatedstreamingspace.md).
- Manages the connection life cycle and handles errors.

You can use the Foveated Streaming App template in Xcode to get started quickly. To do so, create a new project in Xcode by choosing File > New > Project. Navigate to the Multiplatform section of the template chooser, and select the Foveated Streaming App template:

![A screenshot of Xcode showing a list of Multiplatform templates to choose from. The Foveated Streaming App template is selected.](https://docs-assets.developer.apple.com/published/4bbc0f86d945016808048680509fb54f/foveated-streaming-app-template%402x.png)

When prompted, specify a name for your project along with other options.

Alternatively, start from the Foveated Streaming sample app. For more information, see [`Creating a foveated streaming client on visionOS`](creating-a-foveated-streaming-client-on-visionos.md).

## See Also

- [Establishing foveated streaming sessions with Apple Vision Pro](establishing-foveated-streaming-sessions-with-apple-vision-pro.md)
  Discover, pair, and manage streaming sessions between Apple Vision Pro and local streaming endpoints by implementing the session management connection protocol.
- [Creating a foveated streaming client on visionOS](creating-a-foveated-streaming-client-on-visionos.md)
  Build a visionOS app that streams high-fidelity immersive content from a computer or the cloud using the Foveated Streaming framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation)*