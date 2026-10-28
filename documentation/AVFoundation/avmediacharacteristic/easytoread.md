# easyToRead

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let easyToRead: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicEasyToRead;
```

## Discussion

Closed caption tracks that carry “easy reader” captions, as the CEA-608 specification defines, should have this characteristic.

The value of this characteristic is `public.easy-to-read`.

For QuickTime movies and `.m4v` files, a track has this characteristic only if the media’s author tags it that way.

## See Also

### Legible
- [static let legible: AVMediaCharacteristic](./legible.md)
  A media characteristic that indicates that a track or media selection option includes legible content.
- [static let describesVideoForAccessibility: AVMediaCharacteristic](./describesvideoforaccessibility.md)
  A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [static let containsOnlyForcedSubtitles: AVMediaCharacteristic](./containsonlyforcedsubtitles.md)
  A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [static let languageTranslation: AVMediaCharacteristic](./languagetranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [static let transcribesSpokenDialogForAccessibility: AVMediaCharacteristic](./transcribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/easytoread)*