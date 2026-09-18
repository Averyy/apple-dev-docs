# signLanguageInterpretationForAccessibility

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that a track or media selection option provides a sign language interpretation of the spoken dialog and other significant aspects of the presentation.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
static let signLanguageInterpretationForAccessibility: AVMediaCharacteristic
```

#### Discussion

See -[AVAssetTrack hasMediaCharacteristic:] and -[AVMediaSelectionOption hasMediaCharacteristic:]. The value of this characteristic is @“public.accessibility.sign-language-interpretation”. Note for content authors: for QuickTime movie and .m4v files a media option is considered to have the characteristic AVMediaCharacteristicSignLanguageInterpretationForAccessibility only if it’s explicitly tagged with that characteristic. See the discussion of the tagging of tracks with media characteristics below.

Also see -[AVAssetTrack hasMediaCharacteristic:] and -[AVMediaSelectionOption hasMediaCharacteristic:].


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/signlanguageinterpretationforaccessibility)*