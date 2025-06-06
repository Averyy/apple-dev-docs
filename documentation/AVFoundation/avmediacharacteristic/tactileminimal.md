# tactileMinimal

**Framework**: Avfoundation  
**Kind**: property

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

#### Discussion

The value of this characteristic is `public.haptics.minimal`. Query the [`hasMediaCharacteristic(_:)`](avassettrack/hasmediacharacteristic(_:).md) method of [`AVAssetTrack`](avassettrack.md) or the [`hasMediaCharacteristic(_:)`](avmediaselectionoption/hasmediacharacteristic(_:).md) of [`AVMediaSelectionOption`](avmediaselectionoption.md) to determine whether the media contains this characteristic.

> **Note**:  A QuickTime movie or MPEG-4 file track contains this characteristic only when the author explicitly tags it that way.

## See Also

- [static let audible: AVMediaCharacteristic](avmediacharacteristic/audible.md)
  A media characteristic that indicates that a track or media selection option includes audible content.
- [static let dubbedTranslation: AVMediaCharacteristic](avmediacharacteristic/dubbedtranslation.md)
  A media characteristic that indicates that a track or media selection option contains audio language or dialect translation of the original content.
- [static let voiceOverTranslation: AVMediaCharacteristic](avmediacharacteristic/voiceovertranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language translation and verbal interpretation of spoken dialog.
- [static let enhancesSpeechIntelligibility: AVMediaCharacteristic](avmediacharacteristic/enhancesspeechintelligibility.md)
  A media characteristic that indicates a track or media selection option includes audio processed to enhance the intelligibility of speech.
- [static let describesMusicAndSoundForAccessibility: AVMediaCharacteristic](avmediacharacteristic/describesmusicandsoundforaccessibility.md)
  A media characteristic that indicates that a track or media selection option includes legible content in the language of its specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/tactileminimal)*