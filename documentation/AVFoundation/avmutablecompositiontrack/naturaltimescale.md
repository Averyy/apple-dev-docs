# naturalTimeScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time scale in which you can perform time-based operations without extra numerical conversion.

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
var naturalTimeScale: CMTimeScale { get set }
```

```objc
@property (nonatomic) CMTimeScale naturalTimeScale;
```

#### Discussion

If not set, the value is the natural time scale of the first non-empty edit, or 600 if there are no non-empty edits.

Set the value to `0` to revert to the default behavior.

## See Also

### Configuring track properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the tracks is in an enabled state.
- [var languageCode: String?](./languagecode.md)
  The language associated with the track, as an ISO 639-2/T language code.
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The language tag associated with the track, as an RFC 4646 language tag.
- [var preferredTransform: CGAffineTransform](./preferredtransform.md)
  The preferred transformation of the visual media data for display purposes.
- [var preferredVolume: Float](./preferredvolume.md)
  The volume the track prefers for its audible media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/naturaltimescale)*