# MediaEnvironment

**Framework**: BrowserEngineKit  
**Kind**: struct  
**Role**: Structure

An object that identifies a media playback or streaming environment.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct MediaEnvironment
```

#### Overview

To stream media in your browser app, create an instance of `MediaEnvironment` and call [`activate()`](./mediaenvironment/activate%28%29.md) before beginning media playback or capture, for example, by calling the [`AVCaptureSession`](../AVFoundation/avcapturesession.md) class’s [`makeCaptureSession()`](./mediaenvironment/makecapturesession%28%29.md) method.

To finish media playback or capture, call [`suspend()`](./mediaenvironment/suspend%28%29.md).

If your app captures media input or prepares streaming content in a rendering extension, call [`activate()`](./mediaenvironment/activate%28%29.md) before [`grantCapability(_:)`](./renderingprocess/grantcapability%28_%29.md) to grant the media playback and capture capability, which you create with [`ProcessCapability.mediaPlaybackAndCapture(environment:)`](./processcapability/mediaplaybackandcapture%28environment%29.md).

Call [`createXPCRepresentation()`](./mediaenvironment/createxpcrepresentation%28%29.md) and use [XPC](../XPC/XPC.md) to send the media environment to a rendering extension. Additionally, grant the same capability to the web content extension for a page that plays or captures media by calling [`grantCapability(_:)`](./webcontentprocess/grantcapability%28_%29.md).

## Topics

### Creating a media environment
- [init(webPage: URL)](./mediaenvironment/init%28webpage%29.md)
  Creates a new media environment identified by the URL.
- [init(xpcRepresentation: xpc_object_t) throws](./mediaenvironment/init%28xpcrepresentation%29.md)
  Creates a media environment from an XPC representation.
### Sending media environments over XPC connections
- [func createXPCRepresentation() -> xpc_object_t](./mediaenvironment/createxpcrepresentation%28%29.md)
  Creates an encoded representation of the media environment for transmission through an XPC connection.
### Capturing media streams
- [func activate() throws](./mediaenvironment/activate%28%29.md)
  Activates the media environment.
- [func makeCaptureSession() throws -> AVCaptureSession](./mediaenvironment/makecapturesession%28%29.md)
  Creates a new capture session in this media environment  or throws an error if it can not be created.
- [func suspend() throws](./mediaenvironment/suspend%28%29.md)
  Suspends the media environment.

## See Also

### Extension capabilities
- [enum ProcessCapability](./processcapability.md)
  Capabilities of a helper extension process.
- [class BEProcessCapability](./beprocesscapability-76ijx.md)
  Capabilities of a helper extension process.
- [class BEMediaEnvironment](./bemediaenvironment-15xci.md)
  An object that identifies a media playback or streaming environment.
- [class BEWebContentFilter](./bewebcontentfilter.md)
  An object that represents a web content filter.
- [enum RenderingExtensionFeature](./renderingextensionfeature.md)
  Features of a rendering extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/mediaenvironment)*