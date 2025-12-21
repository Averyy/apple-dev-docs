# AVAudioSession.CategoryOptions

**Framework**: AVFAudio  
**Kind**: struct

Constants that specify optional audio behaviors.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CategoryOptions
```

#### Overview

Each option is valid only for specific audio session categories.

## Topics

### Category options
- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
- [static var allowBluetoothA2DP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetootha2dp.md)
  An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).
- [static var allowBluetoothHFP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp.md)
  An option that makes Bluetooth Hands-Free Profile (HFP) devices available for audio input.
- [static var bluetoothHighQualityRecording: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/bluetoothhighqualityrecording.md)
  An option that indicates to enable high-quality audio for input and output routes.
- [static var defaultToSpeaker: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md)
  An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.
- [static var duckOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var farFieldInput: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/farfieldinput.md)
  This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and [`record`](avaudiosession/category-swift.struct/record.md).
- [static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers.md)
  An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.
- [static var mixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.
### Initializers
- [init(rawValue: UInt)](avaudiosession/categoryoptions-swift.struct/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var category: AVAudioSession.Category](avaudiosession/category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](avaudiosession/availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](avaudiosession/category-swift.struct.md)
  Audio session category identifiers.
- [var categoryOptions: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct)*