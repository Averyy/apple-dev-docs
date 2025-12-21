# ReplayKit

**Framework**: ReplayKit  
**Kind**: module

Record or stream video from the screen, and audio from the app and microphone.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

#### Overview

Using the ReplayKit framework, users can record video from the screen, and audio from the app and microphone. They can then share their recordings with other users through email, messages, and social media. You can build app extensions for live broadcasting your content to sharing services. ReplayKit is incompatible with [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) content.

## Topics

### Replay Sharing
- [Recording and Streaming Your macOS App](recording-and-streaming-your-macos-app.md)
  Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.
- [class RPScreenRecorder](rpscreenrecorder.md)
  The shared recorder object that provides the ability to record audio and video of your app.
- [class RPPreviewViewController](rppreviewviewcontroller.md)
  An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit.
### Media Clip Processing
- [class RPBroadcastController](rpbroadcastcontroller.md)
  An object containing methods for starting and controlling a broadcast.
- [class RPBroadcastHandler](rpbroadcasthandler.md)
  An object that sends messages to the broadcasting app.
- [class RPBroadcastSampleHandler](rpbroadcastsamplehandler.md)
  An object that processes buffer objects as received from ReplayKit.
- [class RPBroadcastMP4ClipHandler](rpbroadcastmp4cliphandler.md)
  An object that processes MP4 movie clips from ReplayKit.
### Live Broadcast Implementation
- [class RPBroadcastActivityViewController](rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.
### Errors
- [enum RPRecordingErrorCode](rprecordingerrorcode.md)
  The ReplayKit error domain codes.
- [let RPRecordingErrorDomain: String](rprecordingerrordomain.md)
  The ReplayKit error domain.
- [let SCStreamErrorDomain: String](scstreamerrordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ReplayKit)*