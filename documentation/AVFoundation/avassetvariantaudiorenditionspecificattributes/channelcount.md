# channelCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The count of audio channels in the rendition.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (nonatomic, readonly) NSInteger channelCount;
```

## See Also

### Accessing attributes
- [var isBinaural: Bool](../avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural.md)
  A Boolean value that indicates the variant is best suited for delivery to headphones.
- [var isImmersive: Bool](../avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive.md)
  A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [var isDownmix: Bool](../avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix.md)
  A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantaudiorenditionspecificattributes/channelcount)*