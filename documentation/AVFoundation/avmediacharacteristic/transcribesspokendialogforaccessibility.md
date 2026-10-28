# transcribesSpokenDialogForAccessibility

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.

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
static let transcribesSpokenDialogForAccessibility: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicTranscribesSpokenDialogForAccessibility;
```

## Discussion

Legible media options may include transcriptions of spoken dialog and descriptions of music and sound effects.

The value of this characteristic is `public.accessibility.transcribes-spoken-dialog`.

For QuickTime movies and `.m4v` files, a media option has this characteristic only if the media’s author tags it that way.

## See Also

### Legible
- [static let legible: AVMediaCharacteristic](./legible.md)
  A media characteristic that indicates that a track or media selection option includes legible content.
- [static let easyToRead: AVMediaCharacteristic](./easytoread.md)
  A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [static let describesVideoForAccessibility: AVMediaCharacteristic](./describesvideoforaccessibility.md)
  A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [static let containsOnlyForcedSubtitles: AVMediaCharacteristic](./containsonlyforcedsubtitles.md)
  A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [static let languageTranslation: AVMediaCharacteristic](./languagetranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/transcribesspokendialogforaccessibility)*