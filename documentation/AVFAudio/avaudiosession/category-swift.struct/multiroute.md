# multiRoute

**Framework**: AVFAudio  
**Kind**: property

The category for routing distinct streams of audio data to different output devices at the same time.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let multiRoute: AVAudioSession.Category
```

#### Discussion

This category can be used for input, output, or both. For example, use this category to route audio to both a USB device and a set of headphones. Use of this category requires a more detailed knowledge of, and interaction with, the capabilities of the available audio routes.

> ❗ **Important**:  Route changes can invalidate part or all of your multi-route configuration.  When using the [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md) category, it is essential that you register to observe [`routeChangeNotification`](avaudiosession/routechangenotification.md) notifications and update your configuration as necessary.

 Route changes can invalidate part or all of your multi-route configuration.  When using the [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md) category, it is essential that you register to observe [`routeChangeNotification`](avaudiosession/routechangenotification.md) notifications and update your configuration as necessary.

## See Also

- [static let ambient: AVAudioSession.Category](avaudiosession/category-swift.struct/ambient.md)
  The category for an app in which sound playback is nonprimary — that is, your app also works with the sound turned off.
- [static let playAndRecord: AVAudioSession.Category](avaudiosession/category-swift.struct/playandrecord.md)
  The category for recording (input) and playback (output) of audio, such as for a Voice over Internet Protocol (VoIP) app.
- [static let playback: AVAudioSession.Category](avaudiosession/category-swift.struct/playback.md)
  The category for playing recorded music or other sounds that are central to the successful use of your app.
- [static let record: AVAudioSession.Category](avaudiosession/category-swift.struct/record.md)
  The category for recording audio while also silencing playback audio.
- [static let soloAmbient: AVAudioSession.Category](avaudiosession/category-swift.struct/soloambient.md)
  The default audio session category.
- [static let audioProcessing: AVAudioSession.Category](avaudiosession/category-swift.struct/audioprocessing.md)
  The category for using an audio hardware codec or signal processor while not playing or recording audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct/multiroute)*