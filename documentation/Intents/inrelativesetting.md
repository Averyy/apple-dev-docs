# INRelativeSetting

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating relative settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INRelativeSetting
```

```c
enum INRelativeSetting : NSInteger;
```

## Topics

### Constants
- [INRelativeSetting.unknown](./inrelativesetting/unknown.md)
  An unknown setting.
- [INRelativeSetting.lowest](./inrelativesetting/lowest.md)
  The lowest setting.
- [INRelativeSetting.lower](./inrelativesetting/lower.md)
  The next lower setting.
- [INRelativeSetting.higher](./inrelativesetting/higher.md)
  The next higher setting.
- [INRelativeSetting.highest](./inrelativesetting/highest.md)
  The highest setting.
### Initializers
- [init?(rawValue: Int)](./inrelativesetting/init%28rawvalue%29.md)

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
- [enum INCarAudioSource](./incaraudiosource.md)
  Constants indicating the source of audio.
- [enum INCarAirCirculationMode](./incaraircirculationmode.md)
  Constants indicating the circulation mode for the climate system.
- [enum INRadioType](./inradiotype.md)
  Constants indicating the type of radio.
- [enum INRelativeReference](./inrelativereference.md)
  Constants indicating relative positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelativesetting)*