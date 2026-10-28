# predicate(forDownmixAudio:mediaSelectionOption:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a predicate for downmix audio.

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
class func predicate(forDownmixAudio isDownmixAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForDownmixAudio:(BOOL) isDownmixAudio mediaSelectionOption:(AVMediaSelectionOption *) mediaSelectionOption;
```

## Return Value

A predicate object that you use to to create an [`AVAssetVariantQualifier`](../avassetvariantqualifier.md).

## Discussion

Use the returned value, along with other predicates, to express variant preferences.

## Parameters

- `isDownmixAudio`: 
- `mediaSelectionOption`: The media selection option for the variant.

## See Also

### Building predicates
- [class func predicate(forAudioSampleRate: Double, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./predicate%28foraudiosamplerate,mediaselectionoption,operatortype%29.md)
  Creates a predicate for audio sample rate.
- [class func predicate(forAudioSampleRate: Double, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./predicate%28foraudiosamplerate,operatortype%29.md)
  Creates a NSPredicate for audio sample rate which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forBinauralAudio: Bool) -> NSPredicate](./predicate%28forbinauralaudio%29.md)
  Creates a NSPredicate for binaural which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forBinauralAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](./predicate%28forbinauralaudio,mediaselectionoption%29.md)
  Creates a predicate for binaural audio.
- [class func predicate(forChannelCount: Int, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./predicate%28forchannelcount,mediaselectionoption,operatortype%29.md)
  Creates a predicate with a channel count, media selection option, and operator type.
- [class func predicate(forChannelCount: Int, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./predicate%28forchannelcount,operatortype%29.md)
  Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forDownmixAudio: Bool) -> NSPredicate](./predicate%28fordownmixaudio%29.md)
  Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forImmersiveAudio: Bool) -> NSPredicate](./predicate%28forimmersiveaudio%29.md)
  Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.
- [class func predicate(forImmersiveAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](./predicate%28forimmersiveaudio,mediaselectionoption%29.md)
  Creates a predicate for immersive audio.
- [class func predicate(forPresentationHeight: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./predicate%28forpresentationheight,operatortype%29.md)
  Creates a predicate with a height and operator type.
- [class func predicate(forPresentationWidth: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./predicate%28forpresentationwidth,operatortype%29.md)
  Creates a predicate with a width and operator type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(fordownmixaudio:mediaselectionoption:))*