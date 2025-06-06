# AVMediaCharacteristic

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines media data characteristics.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVMediaCharacteristic
```

#### Discussion

QuickTime Movie and MPEG-4 video files may contain tracks that provide tagged media characteristics to indicate a purpose, trait, or feature of the track’s media. For example, an audio track that mixes original program content with additional narrative descriptions of visual action may have the media characteristic `public.accessibility.describes-video` to distinguish it from other audio tracks stored in the same file that don’t contain additional narrative.

You inspect the tagged media characteristics of a track as shown below:

```objc
NSArray *userDataItems = [myAVAssetTrack metadataForFormat:AVMetadataFormatQuickTimeUserData];
NSArray *trackTaggedMediaCharacteristics = [AVMetadataItem metadataItemsFromArray: userDataItems
        withKey: AVMetadataQuickTimeUserDataKeyTaggedCharacteristic
        keySpace: AVMetadataKeySpaceQuickTimeUserData];
for (AVMetadataItem *metadataItem in trackTaggedMediaCharacteristics) {
     NSString *thisTrackMediaCharacteristic = [metadataItem stringValue];
}
```

You write tagged media characteristics to files of type [`mov`](avfiletype/mov.md) and [`m4v`](avfiletype/m4v.md) by using an instance of [`AVAssetWriter`](avassetwriter.md). You indicate tagged characteristics for a track by setting metadata on its associated asset writer input as shown below:

```objc
AVMutableMetadataItem *myTaggedMediaCharacteristic = [[AVMutableMetadataItem alloc] init];
[myTaggedMediaCharacteristic setKey:AVMetadataQuickTimeUserDataKeyTaggedCharacteristic];
[myTaggedMediaCharacteristic setKeySpace:AVMetadataKeySpaceQuickTimeUserData];
[myTaggedMediaCharacteristic setValue:aMeaningfulCharacteristicAsNSString];
[myMutableArrayOfMetadata addObject:myTaggedMediaCharacteristic];
[myAssetWriterInput setMetadata:myMutableArrayOfMetadata];
```

## Topics

### Visual
- [static let visual: AVMediaCharacteristic](avmediacharacteristic/visual.md)
  A media characteristic that indicates that a track or media selection option includes visual content.
- [static let containsAlphaChannel: AVMediaCharacteristic](avmediacharacteristic/containsalphachannel.md)
  A media characteristic that indicates that a track contains an alpha channel.
- [static let containsHDRVideo: AVMediaCharacteristic](avmediacharacteristic/containshdrvideo.md)
  A media characteristic that indicates that a track contains HDR video.
- [static let frameBased: AVMediaCharacteristic](avmediacharacteristic/framebased.md)
  A media characteristic that indicates that a track or media selection option includes frame-based content.
- [static let usesWideGamutColorSpace: AVMediaCharacteristic](avmediacharacteristic/useswidegamutcolorspace.md)
  A media characteristic that indicates that a track uses a wide-gamut color space.
- [static let containsStereoMultiviewVideo: AVMediaCharacteristic](avmediacharacteristic/containsstereomultiviewvideo.md)
  A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [static let carriesVideoStereoMetadata: AVMediaCharacteristic](avmediacharacteristic/carriesvideostereometadata.md)
  A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [static let indicatesHorizontalFieldOfView: AVMediaCharacteristic](avmediacharacteristic/indicateshorizontalfieldofview.md)
  A media characteristic that indicates the video track carries information related to the horizontal field of view.
### Audible
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
- [static let tactileMinimal: AVMediaCharacteristic](avmediacharacteristic/tactileminimal.md)
  A media characteristic that indicates that a track or media selection option includes haptic content.
### Legible
- [static let legible: AVMediaCharacteristic](avmediacharacteristic/legible.md)
  A media characteristic that indicates that a track or media selection option includes legible content.
- [static let easyToRead: AVMediaCharacteristic](avmediacharacteristic/easytoread.md)
  A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [static let describesVideoForAccessibility: AVMediaCharacteristic](avmediacharacteristic/describesvideoforaccessibility.md)
  A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [static let containsOnlyForcedSubtitles: AVMediaCharacteristic](avmediacharacteristic/containsonlyforcedsubtitles.md)
  A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [static let languageTranslation: AVMediaCharacteristic](avmediacharacteristic/languagetranslation.md)
  A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [static let transcribesSpokenDialogForAccessibility: AVMediaCharacteristic](avmediacharacteristic/transcribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.
### Content
- [static let isOriginalContent: AVMediaCharacteristic](avmediacharacteristic/isoriginalcontent.md)
  A media characteristic that indicates that a track or media selection option contains original content.
- [static let isMainProgramContent: AVMediaCharacteristic](avmediacharacteristic/ismainprogramcontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [static let isAuxiliaryContent: AVMediaCharacteristic](avmediacharacteristic/isauxiliarycontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
### Initializers
- [init(String)](avmediacharacteristic/init(_:).md)
  Creates a media characteristic.
- [init(rawValue: String)](avmediacharacteristic/init(rawvalue:).md)
  Creates a media characteristic with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AVMediaType](avmediatype.md)
  An identifier for various media types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic)*