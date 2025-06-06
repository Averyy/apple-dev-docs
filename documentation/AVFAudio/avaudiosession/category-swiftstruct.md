# AVAudioSession.Category

**Framework**: AVFAudio  
**Kind**: struct

Audio session category identifiers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct Category
```

#### Discussion

An audio session category defines a set of audio behaviors. Choose a category that most accurately describes the audio behavior you require.

##### Supporting Airplay

The playback-only categories ([`ambient`](avaudiosession/category-swift.struct/ambient.md), [`soloAmbient`](avaudiosession/category-swift.struct/soloambient.md), and [`playback`](avaudiosession/category-swift.struct/playback.md)) support both the mirrored and nonmirrored variants of AirPlay.

The audio session category [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) supports only the mirrored variant of AirPlay, while the [`record`](avaudiosession/category-swift.struct/record.md) and [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md) categories don’t allow routing to AirPlay.

> ❗ **Important**:  SharePlay and the Group Activities API only support audio sessions using the [`playback`](avaudiosession/category-swift.struct/playback.md) category. Attempting to activate a session that uses an unsupported category results in an error.

 SharePlay and the Group Activities API only support audio sessions using the [`playback`](avaudiosession/category-swift.struct/playback.md) category. Attempting to activate a session that uses an unsupported category results in an error.

## Topics

### Creating a Category
- [init(rawValue: String)](avaudiosession/category-swift.struct/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard Categories
- [static let ambient: AVAudioSession.Category](avaudiosession/category-swift.struct/ambient.md)
  The category for an app in which sound playback is nonprimary — that is, your app also works with the sound turned off.
- [static let multiRoute: AVAudioSession.Category](avaudiosession/category-swift.struct/multiroute.md)
  The category for routing distinct streams of audio data to different output devices at the same time.
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

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var category: AVAudioSession.Category](avaudiosession/category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](avaudiosession/availablecategories.md)
  The audio session categories available on the current device.
- [var categoryOptions: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct)*