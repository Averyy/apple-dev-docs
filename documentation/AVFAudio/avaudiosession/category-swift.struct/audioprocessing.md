# audioProcessing

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

The category for using an audio hardware codec or signal processor while not playing or recording audio.

**Availability**:
- iOS 3.0+ - Deprecated in 10.0
- iPadOS 3.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This category is no longer necessary and was deprecated iOS 10.

## Declaration

```swift
static let audioProcessing: AVAudioSession.Category
```

```c
extern AVAudioSessionCategory const AVAudioSessionCategoryAudioProcessing;
```

#### Discussion

This category disables playback (audio output) and disables recording (audio input). Use this category, for example, when performing offline audio format conversion.

## See Also

### Getting standard categories
- [static let ambient: AVAudioSession.Category](./ambient.md)
  The category for an app in which sound playback is nonprimary — that is, your app also works with the sound turned off.
- [static let multiRoute: AVAudioSession.Category](./multiroute.md)
  The category for routing distinct streams of audio data to different output devices at the same time.
- [static let playAndRecord: AVAudioSession.Category](./playandrecord.md)
  The category for recording (input) and playback (output) of audio, such as for a Voice over Internet Protocol (VoIP) app.
- [static let playback: AVAudioSession.Category](./playback.md)
  The category for playing recorded music or other sounds that are central to the successful use of your app.
- [static let record: AVAudioSession.Category](./record.md)
  The category for recording audio while also silencing playback audio.
- [static let soloAmbient: AVAudioSession.Category](./soloambient.md)
  The default audio session category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct/audioprocessing)*