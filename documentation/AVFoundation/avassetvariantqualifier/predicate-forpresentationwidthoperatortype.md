# predicate(forPresentationWidth:operatorType:)

**Framework**: AVFoundation  
**Kind**: method

Creates a predicate with a width and operator type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class func predicate(forPresentationWidth width: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate
```

#### Return Value

A predicate object that you use to to create an [`AVAssetVariantQualifier`](avassetvariantqualifier.md).

## Parameters

- `width`: The presentation width.
- `operatorType`: The predicate’s operator type.

## See Also

- [class func predicate(forAudioSampleRate: Double, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(foraudiosamplerate:mediaselectionoption:operatortype:).md)
  Creates a predicate for audio sample rate.
- [class func predicate(forAudioSampleRate: Double, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(foraudiosamplerate:operatortype:).md)
  Creates a NSPredicate for audio sample rate which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forBinauralAudio: Bool) -> NSPredicate](avassetvariantqualifier/predicate(forbinauralaudio:).md)
  Creates a NSPredicate for binaural which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forBinauralAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](avassetvariantqualifier/predicate(forbinauralaudio:mediaselectionoption:).md)
  Creates a predicate for binaural audio.
- [class func predicate(forChannelCount: Int, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forchannelcount:mediaselectionoption:operatortype:).md)
  Creates a predicate with a channel count, media selection option, and operator type.
- [class func predicate(forChannelCount: Int, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forchannelcount:operatortype:).md)
  Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forDownmixAudio: Bool) -> NSPredicate](avassetvariantqualifier/predicate(fordownmixaudio:).md)
  Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forDownmixAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](avassetvariantqualifier/predicate(fordownmixaudio:mediaselectionoption:).md)
  Creates a predicate for downmix audio.
- [class func predicate(forImmersiveAudio: Bool) -> NSPredicate](avassetvariantqualifier/predicate(forimmersiveaudio:).md)
  Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forImmersiveAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](avassetvariantqualifier/predicate(forimmersiveaudio:mediaselectionoption:).md)
  Creates a predicate for immersive audio.
- [class func predicate(forPresentationHeight: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forpresentationheight:operatortype:).md)
  Creates a predicate with a height and operator type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forpresentationwidth:operatortype:))*