# AVAudioSession.Category

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Audio session category identifiers.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct Category
```

```c
typedef NSString * AVAudioSessionCategory;
```

## Discussion

An audio session category defines a set of audio behaviors. Choose a category that most accurately describes the audio behavior you require.

### Supporting AirPlay

The playback-only categories ([`ambient`](./category-swift.struct/ambient.md), [`soloAmbient`](./category-swift.struct/soloambient.md), and [`playback`](./category-swift.struct/playback.md)) support both the mirrored and nonmirrored variants of AirPlay.

The audio session category [`playAndRecord`](./category-swift.struct/playandrecord.md) supports only the mirrored variant of AirPlay, while the [`record`](./category-swift.struct/record.md) and [`multiRoute`](./category-swift.struct/multiroute.md) categories don’t allow routing to AirPlay.

> ❗ **Important**:  SharePlay and the Group Activities API only support audio sessions using the [`playback`](./category-swift.struct/playback.md) category. Attempting to activate a session that uses an unsupported category results in an error.

## Topics

### Creating a category
- [init(rawValue: String)](./category-swift.struct/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting standard categories
- [static let ambient: AVAudioSession.Category](./category-swift.struct/ambient.md)
  The category for an app in which sound playback is nonprimary — that is, your app also works with the sound turned off.
- [static let multiRoute: AVAudioSession.Category](./category-swift.struct/multiroute.md)
  The category for routing distinct streams of audio data to different output devices at the same time.
- [static let playAndRecord: AVAudioSession.Category](./category-swift.struct/playandrecord.md)
  The category for recording (input) and playback (output) of audio, such as for a Voice over Internet Protocol (VoIP) app.
- [static let playback: AVAudioSession.Category](./category-swift.struct/playback.md)
  The category for playing recorded music or other sounds that are central to the successful use of your app.
- [static let record: AVAudioSession.Category](./category-swift.struct/record.md)
  The category for recording audio while also silencing playback audio.
- [static let soloAmbient: AVAudioSession.Category](./category-swift.struct/soloambient.md)
  The default audio session category.
- [static let audioProcessing: AVAudioSession.Category](./category-swift.struct/audioprocessing.md)
  The category for using an audio hardware codec or signal processor while not playing or recording audio.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the category configuration
- [var category: AVAudioSession.Category](./category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](./availablecategories.md)
  The audio session categories available on the current device.
- [var categoryOptions: AVAudioSession.CategoryOptions](./categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](./categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.struct)*