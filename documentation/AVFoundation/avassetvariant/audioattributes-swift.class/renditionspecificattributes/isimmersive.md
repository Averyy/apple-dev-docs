# isImmersive

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.

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
var isImmersive: Bool { get }
```

#### Discussion

If a variant audio redition is immersive it’s eligible for rendering to headphones or speakers.

## See Also

- [var channelCount: Int?](avassetvariant/audioattributes-swift.class/renditionspecificattributes/channelcount.md)
  The count of audio channels in the rendition.
- [var isBinaural: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural.md)
  A Boolean value that indicates the variant is best suited for delivery to headphones.
- [var isDownmix: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix.md)
  A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive)*