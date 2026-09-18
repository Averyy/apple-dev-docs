# AVKit

**Framework**: AVKit  
**Kind**: module

Adopt the system’s video playback interfaces, and integrate your camera app with capture hardware.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Mentions

- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Overview

AVKit provides the interfaces your app uses to integrate media with the hardware and software of an Apple device. For playback, it provides the system’s standard video player, so your app presents video the way people already expect instead of designing an interface of its own. For capture, it provides the integration points that connect a camera app to capture hardware and to the system features that surround it.

It builds on [`AVFoundation`](https://developer.apple.com/documentation/avfoundation), which does the work of playing and capturing media. Implement your app’s media features with AVFoundation, then adopt AVKit so those features work the way the rest of the device does.

## Topics

### Essentials
- [Playback interfaces](avkit-playback-interfaces.md)
  Present video with the system player, complete with transport controls and Picture in Picture.
- [Capture interfaces](avkit-capture-interfaces.md)
  Capture from hardware buttons and AirPods, present an audio input picker, and connect a nearby iPhone as a camera.
### Errors
- [let AVKitErrorDomain: String](avkiterrordomain.md)
  The domain of errors the framework generates.
- [struct AVKitError](avkiterror-swift.struct.md)
  A structure that represents a framework error.
- [AVKitError.Code](avkiterror-swift.struct/code.md)
  Constants that identify framework error codes.
- [Error constants](error-constants.md)
  Error code constants for framework operations.
### Macros
- [Macros](avkit-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVKit)*