# AVAssetVariantQualifier

**Framework**: AVFoundation  
**Kind**: class

An object that represents an HTTP Live Streaming asset variant.

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
class AVAssetVariantQualifier
```

## Topics

### Creating a variant qualifier
- [convenience init(variant: AVAssetVariant)](avassetvariantqualifier/init(variant:).md)
  Creates a variant qualifier with an asset variant.
- [class AVAssetVariant](avassetvariant.md)
  An object that represents a bit rate variant.
- [convenience init(predicate: NSPredicate)](avassetvariantqualifier/init(predicate:).md)
  Creates a variant qualifier with a predicate.
### Building predicates
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
- [class func predicate(forPresentationWidth: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forpresentationwidth:operatortype:).md)
  Creates a predicate with a width and operator type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var variantQualifiers: [AVAssetVariantQualifier]](avassetdownloadcontentconfiguration/variantqualifiers.md)
  The variant qualifiers for this configuration.
- [var mediaSelections: [AVMediaSelection]](avassetdownloadcontentconfiguration/mediaselections.md)
  The media selections of an asset that a task downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier)*