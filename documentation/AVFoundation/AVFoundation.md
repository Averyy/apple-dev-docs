# AVFoundation

**Framework**: AVFoundation  
**Kind**: module

Work with audiovisual assets, control device cameras, process audio, and configure system audio interactions.

**Availability**:
- iOS 2.2+
- iPadOS 13.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

#### Overview

AVFoundation combines several major technology areas that together encompass a wide range of tasks for inspecting, playing, capturing, and processing audiovisual media on Apple platforms.

## Topics

### Essentials
- [AVFoundation updates](../Updates/AVFoundation.md)
  Learn about important changes to AVFoundation.
### Common
- [Media assets](media-assets.md)
  Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.
- [Media reading and writing](media-reading-and-writing.md)
  Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- [Media types and utilities](media-types-and-utilities.md)
  Identify the types of content and file formats that AVFoundation supports.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.
### Playback
- [Media playback](media-playback.md)
  Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Offline playback and storage](offline-playback-and-storage.md)
  Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.
- [Streaming and AirPlay](streaming-and-airplay.md)
  Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.
- [Sample buffer playback](sample-buffer-playback.md)
  Create custom controllers to play and synchronize the timing of sample buffer streams.
### Capture
- [Capture setup](capture-setup.md)
  Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Photo capture](photo-capture.md)
  Capture high-quality still images, Live Photos, and supporting photo data.
- [Audio and video capture](audio-and-video-capture.md)
  Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.
- [Additional data capture](additional-data-capture.md)
  Capture additional data including depth and metadata, and synchronize capture from multiple outputs.
### Editing
- [Composite assets](composite-assets.md)
  Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- [QuickTime movies](quicktime-movies.md)
  Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.
- [Video effects](video-effects.md)
  Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.
- [Audio mixing](audio-mixing.md)
  Define how to mix the audio levels from multiple audio tracks over an asset’s duration.
### Audio
- [Audio playback, recording, and processing](audio-playback-recording-and-processing.md)
  Play, record, and process audio; configure your app’s system audio behavior.
- [Speech synthesis](speech-synthesis.md)
  Configure voices to speak strings of text.
### Errors
- [let AVFoundationErrorDomain: String](avfoundationerrordomain.md)
  The error domain of AVFoundation errors.
- [struct AVError](averror-swift.struct.md)
  A structure that defines the errors that framework operations can generate.
### Macros
- [Macros](avfoundation-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFoundation)*