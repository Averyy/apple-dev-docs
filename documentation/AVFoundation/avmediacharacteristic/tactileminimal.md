# tactileMinimal

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a track or media selection option includes haptic content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let tactileMinimal: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicTactileMinimal;
```

#### Discussion

The value of this characteristic is `public.haptics.minimal`. Query the [`hasMediaCharacteristic(_:)`](../avassettrack/hasmediacharacteristic%28_%29.md) method of [`AVAssetTrack`](../avassettrack.md) or the [`hasMediaCharacteristic(_:)`](../avmediaselectionoption/hasmediacharacteristic%28_%29.md) of [`AVMediaSelectionOption`](../avmediaselectionoption.md) to determine whether the media contains this characteristic.

> **Note**:  A QuickTime movie or MPEG-4 file track contains this characteristic only when the author explicitly tags it that way.

## See Also

### Audible
- [static let audible: AVMediaCharacteristic](./audible.md)
  A media characteristic that indicates that a track or media selection option includes audible content.
- [static let dubbedTranslation: AVMediaCharacteristic](./dubbedtranslation.md)
  A media characteristic that indicates that a track or media selection option contains audio language or dialect translation of the original content.
- [static let voiceOverTranslation: AVMediaCharacteristic](./voiceovertranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language translation and verbal interpretation of spoken dialog.
- [static let enhancesSpeechIntelligibility: AVMediaCharacteristic](./enhancesspeechintelligibility.md)
  A media characteristic that indicates a track or media selection option includes audio processed to enhance the intelligibility of speech.
- [static let describesMusicAndSoundForAccessibility: AVMediaCharacteristic](./describesmusicandsoundforaccessibility.md)
  A media characteristic that indicates that a track or media selection option includes legible content in the language of its specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/tactileminimal)*