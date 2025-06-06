# predicate(forPresentationHeight:operatorType:)

**Framework**: AVFoundation  
**Kind**: method

Creates a predicate with a height and operator type.

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
class func predicate(forPresentationHeight height: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate
```

#### Return Value

A predicate object that you use to to create an [`AVAssetVariantQualifier`](avassetvariantqualifier.md).

## Parameters

- `height`: The presentation height.
- `operatorType`: The predicate’s operator type.

## See Also

- [convenience init(variant: AVAssetVariant)](avassetvariantqualifier/init(variant:).md)
  Creates a variant qualifier with an asset variant.
- [class AVAssetVariant](avassetvariant.md)
  An object that represents a bit rate variant.
- [convenience init(predicate: NSPredicate)](avassetvariantqualifier/init(predicate:).md)
  Creates a variant qualifier with a predicate.
- [class func predicate(forChannelCount: Int, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forchannelcount:mediaselectionoption:operatortype:).md)
  Creates a predicate with a channel count, media selection option, and operator type.
- [class func predicate(forPresentationWidth: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forpresentationwidth:operatortype:).md)
  Creates a predicate with a width and operator type.
- [class func predicate(forBinauralAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](avassetvariantqualifier/predicate(forbinauralaudio:mediaselectionoption:).md)
  Creates a predicate for binaural audio.
- [class func predicate(forDownmixAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](avassetvariantqualifier/predicate(fordownmixaudio:mediaselectionoption:).md)
  Creates a predicate for downmix audio.
- [class func predicate(forImmersiveAudio: Bool, mediaSelectionOption: AVMediaSelectionOption?) -> NSPredicate](avassetvariantqualifier/predicate(forimmersiveaudio:mediaselectionoption:).md)
  Creates a predicate for immersive audio.
- [class func predicate(forAudioSampleRate: Double, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(foraudiosamplerate:mediaselectionoption:operatortype:).md)
  Creates a predicate for audio sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forpresentationheight:operatortype:))*