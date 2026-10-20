# legible

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a track or media selection option includes legible content.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let legible: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicLegible;
```

## Mentions

- [Selecting subtitles and alternative audio tracks](../selecting-subtitles-and-alternative-audio-tracks.md)

#### Discussion

Media types with this characteristic include [`subtitle`](../avmediatype/subtitle.md) and [`closedCaption`](../avmediatype/closedcaption.md).

## See Also

### Legible
- [static let easyToRead: AVMediaCharacteristic](./easytoread.md)
  A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [static let describesVideoForAccessibility: AVMediaCharacteristic](./describesvideoforaccessibility.md)
  A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [static let containsOnlyForcedSubtitles: AVMediaCharacteristic](./containsonlyforcedsubtitles.md)
  A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [static let languageTranslation: AVMediaCharacteristic](./languagetranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [static let transcribesSpokenDialogForAccessibility: AVMediaCharacteristic](./transcribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/legible)*