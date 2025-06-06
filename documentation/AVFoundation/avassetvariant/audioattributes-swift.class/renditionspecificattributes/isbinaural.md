# isBinaural

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates the variant is best suited for delivery to headphones.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isBinaural: Bool { get }
```

#### Discussion

A binaural variant may originate from a direct binaural recording or from the processing of a multichannel audio source.

## See Also

- [var channelCount: Int?](avassetvariant/audioattributes-swift.class/renditionspecificattributes/channelcount.md)
  The count of audio channels in the rendition.
- [var isImmersive: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive.md)
  A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [var isDownmix: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix.md)
  A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural)*