# containsOnlyForcedSubtitles

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that a track or media selection option presents only forced subtitles.

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
static let containsOnlyForcedSubtitles: AVMediaCharacteristic
```

#### Discussion

The value of this characteristic is `public.subtitles.forced-only`.

The system infers this characteristic from the format description of the associated track.

## See Also

- [static let legible: AVMediaCharacteristic](avmediacharacteristic/legible.md)
  A media characteristic that indicates that a track or media selection option includes legible content.
- [static let easyToRead: AVMediaCharacteristic](avmediacharacteristic/easytoread.md)
  A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [static let describesVideoForAccessibility: AVMediaCharacteristic](avmediacharacteristic/describesvideoforaccessibility.md)
  A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [static let languageTranslation: AVMediaCharacteristic](avmediacharacteristic/languagetranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [static let transcribesSpokenDialogForAccessibility: AVMediaCharacteristic](avmediacharacteristic/transcribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containsonlyforcedsubtitles)*