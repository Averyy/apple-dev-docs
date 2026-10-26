# INCarAudioSource

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the source of audio.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INCarAudioSource
```

```c
enum INCarAudioSource : NSInteger;
```

## Topics

### Constants
- [INCarAudioSource.sourceUnknown](./incaraudiosource/sourceunknown.md)
  An unknown source.
- [INCarAudioSource.sourceCarPlay](./incaraudiosource/sourcecarplay.md)
  A CarPlay source.
- [INCarAudioSource.sourceiPod](./incaraudiosource/sourceipod.md)
  An iPod source.
- [INCarAudioSource.sourceRadio](./incaraudiosource/sourceradio.md)
  A radio source.
- [INCarAudioSource.sourceBluetooth](./incaraudiosource/sourcebluetooth.md)
  A source connected over Bluetooth.
- [INCarAudioSource.sourceAUX](./incaraudiosource/sourceaux.md)
  A source connected through an auxiliary jack.
- [INCarAudioSource.sourceUSB](./incaraudiosource/sourceusb.md)
  A source connected through a USB plug.
- [INCarAudioSource.sourceMemoryCard](./incaraudiosource/sourcememorycard.md)
  A memory card source.
- [INCarAudioSource.sourceOpticalDrive](./incaraudiosource/sourceopticaldrive.md)
  An optical drive source such as a CD or DVD.
- [INCarAudioSource.sourceHardDrive](./incaraudiosource/sourceharddrive.md)
  A hard drive source.
### Initializers
- [init?(rawValue: Int)](./incaraudiosource/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### CarPlay Data Objects
- [enum INCarSeat](./incarseat.md)
  Constants indicating a seat position.
- [enum INCarDefroster](./incardefroster.md)
  Constants indicating the defroster type.
- [enum INCarAirCirculationMode](./incaraircirculationmode.md)
  Constants indicating the circulation mode for the climate system.
- [enum INRadioType](./inradiotype.md)
  Constants indicating the type of radio.
- [enum INRelativeReference](./inrelativereference.md)
  Constants indicating relative positions.
- [enum INRelativeSetting](./inrelativesetting.md)
  Constants indicating relative settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incaraudiosource)*