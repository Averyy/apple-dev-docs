# AVAssetVariant

**Framework**: AVFoundation  
**Kind**: class

An object that represents a bit rate variant.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AVAssetVariant
```

## Topics

### Configuring Attributes
- [var audioAttributes: AVAssetVariant.AudioAttributes?](avassetvariant/audioattributes-swift.property.md)
  The audio rendition attributes for the variant.
- [AVAssetVariant.AudioAttributes](avassetvariant/audioattributes-swift.class.md)
  An object that defines the audio attributes for an asset variant.
- [var videoAttributes: AVAssetVariant.VideoAttributes?](avassetvariant/videoattributes-swift.property.md)
  The video rendition attributes for the variant.
- [AVAssetVariant.VideoAttributes](avassetvariant/videoattributes-swift.class.md)
  An object that defines the video attributes for an asset variant.
### Configuring Bit Rate
- [var averageBitRate: Double?](avassetvariant/averagebitrate-5p1oh.md)
  The average bit rate for the variant.
- [var peakBitRate: Double?](avassetvariant/peakbitrate-9hzpi.md)
  The peak bit rate for the variant.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(variant: AVAssetVariant)](avassetvariantqualifier/init(variant:).md)
  Creates a variant qualifier with an asset variant.
- [convenience init(predicate: NSPredicate)](avassetvariantqualifier/init(predicate:).md)
  Creates a variant qualifier with a predicate.
- [class func predicate(forChannelCount: Int, mediaSelectionOption: AVMediaSelectionOption?, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forchannelcount:mediaselectionoption:operatortype:).md)
  Creates a predicate with a channel count, media selection option, and operator type.
- [class func predicate(forPresentationHeight: CGFloat, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](avassetvariantqualifier/predicate(forpresentationheight:operatortype:).md)
  Creates a predicate with a height and operator type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant)*