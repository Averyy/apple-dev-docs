# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property

The language tag associated with the track, as an RFC 4646 language tag.

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
var extendedLanguageTag: String? { get set }
```

#### Discussion

If not set, the value is `nil`.

## See Also

- [var isEnabled: Bool](avmutablecompositiontrack/isenabled.md)
  A Boolean value that indicates whether the tracks is in an enabled state.
- [var naturalTimeScale: CMTimeScale](avmutablecompositiontrack/naturaltimescale.md)
  The time scale in which you can perform time-based operations without extra numerical conversion.
- [var languageCode: String?](avmutablecompositiontrack/languagecode.md)
  The language associated with the track, as an ISO 639-2/T language code.
- [var preferredTransform: CGAffineTransform](avmutablecompositiontrack/preferredtransform.md)
  The preferred transformation of the visual media data for display purposes.
- [var preferredVolume: Float](avmutablecompositiontrack/preferredvolume.md)
  The volume the track prefers for its audible media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/extendedlanguagetag)*