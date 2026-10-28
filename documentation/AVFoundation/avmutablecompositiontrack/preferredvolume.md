# preferredVolume

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The volume the track prefers for its audible media data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var preferredVolume: Float { get set }
```

```objc
@property (nonatomic) float preferredVolume;
```

## Discussion

If not set, the value is `1.0`.

## See Also

### Configuring track properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the tracks is in an enabled state.
- [var naturalTimeScale: CMTimeScale](./naturaltimescale.md)
  The time scale in which you can perform time-based operations without extra numerical conversion.
- [var languageCode: String?](./languagecode.md)
  The language associated with the track, as an ISO 639-2/T language code.
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The language tag associated with the track, as an RFC 4646 language tag.
- [var preferredTransform: CGAffineTransform](./preferredtransform.md)
  The preferred transformation of the visual media data for display purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/preferredvolume)*