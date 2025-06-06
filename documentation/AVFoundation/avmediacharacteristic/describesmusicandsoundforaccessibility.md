# describesMusicAndSoundForAccessibility

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that a track or media selection option includes legible content in the language of its specified locale.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let describesMusicAndSoundForAccessibility: AVMediaCharacteristic
```

#### Discussion

Legible media options may include transcriptions of spoken dialog and descriptions of music and sound effects.

The value of this characteristic is `public.accessibility.describes-music-and-sound`.

For QuickTime movies and `.m4v` files, a media option has this characteristic only if the media’s author tags it that way.

## See Also

- [static let audible: AVMediaCharacteristic](avmediacharacteristic/audible.md)
  A media characteristic that indicates that a track or media selection option includes audible content.
- [static let dubbedTranslation: AVMediaCharacteristic](avmediacharacteristic/dubbedtranslation.md)
  A media characteristic that indicates that a track or media selection option contains audio language or dialect translation of the original content.
- [static let voiceOverTranslation: AVMediaCharacteristic](avmediacharacteristic/voiceovertranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language translation and verbal interpretation of spoken dialog.
- [static let enhancesSpeechIntelligibility: AVMediaCharacteristic](avmediacharacteristic/enhancesspeechintelligibility.md)
  A media characteristic that indicates a track or media selection option includes audio processed to enhance the intelligibility of speech.
- [static let tactileMinimal: AVMediaCharacteristic](avmediacharacteristic/tactileminimal.md)
  A media characteristic that indicates that a track or media selection option includes haptic content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/describesmusicandsoundforaccessibility)*