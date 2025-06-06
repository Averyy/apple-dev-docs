# MediaEnvironment

**Framework**: BrowserEngineKit  
**Kind**: struct

An object that identifies a media playback or streaming environment.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct MediaEnvironment
```

#### Overview

To stream media in your browser app, create an instance of `MediaEnvironment` in the app. In the app, call [`activate()`](mediaenvironment/activate().md) before you begin any media playback or capture, including using the [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) that you get by calling [`makeCaptureSession()`](mediaenvironment/makecapturesession().md). When you are done with the media environment, call [`suspend()`](mediaenvironment/suspend().md).

If you capture media input or prepare streaming content in your browser’s rendering extension, call [`activate()`](mediaenvironment/activate().md) before calling [`grantCapability(_:)`](renderingprocess/grantcapability(_:).md) to grant a media playback and capture capability, which you create with [`ProcessCapability.mediaPlaybackAndCapture(environment:)`](processcapability/mediaplaybackandcapture(environment:).md). Call [`createXPCRepresentation()`](mediaenvironment/createxpcrepresentation().md) and use [`XPC`](https://developer.apple.com/documentation/XPC) to send the media environment to the rendering extension. Additionally, grant the same capability to the web content extension for the page that’s playing or capturing media, by calling [`grantCapability(_:)`](webcontentprocess/grantcapability(_:).md).

## Topics

### Creating a media environment
- [init(webPage: URL)](mediaenvironment/init(webpage:).md)
  Creates a new media environment identified by the URL.
- [init(xpcRepresentation: xpc_object_t) throws](mediaenvironment/init(xpcrepresentation:).md)
  Creates a media environment from an XPC representation.
### Sending media environments over XPC connections
- [func createXPCRepresentation() -> xpc_object_t](mediaenvironment/createxpcrepresentation.md)
  Creates an encoded representation of the media environment, suitable for sending over an XPC connection.
### Capturing media streams
- [func activate() throws](mediaenvironment/activate.md)
  Activates the media environment.
- [func makeCaptureSession() throws -> AVCaptureSession](mediaenvironment/makecapturesession.md)
  Creates a new capture session in this media environment  or throws an error if it can not be created.
- [func suspend() throws](mediaenvironment/suspend.md)
  Suspends the media environment.

## See Also

- [enum ProcessCapability](processcapability.md)
  An enumeration that identifies capabilities that a browser app can grant to its extension processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/mediaenvironment)*