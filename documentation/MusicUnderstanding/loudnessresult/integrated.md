# integrated

**Framework**: MusicUnderstanding  
**Kind**: property

The integrated loudness of the song, measured in LUFS over its full duration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let integrated: MusicUnderstandingSession.TimedValue<Float>
```

## See Also

- [let momentary: [MusicUnderstandingSession.TimedValue<Float>]](loudnessresult/momentary.md)
  An array of momentary loudness measurements sampled across the song in LUFS.
- [let peak: MusicUnderstandingSession.TimedValue<Float>](loudnessresult/peak.md)
  The peak amplitude of the song in decibels (dB).
- [let shortTerm: [MusicUnderstandingSession.TimedValue<Float>]](loudnessresult/shortterm.md)
  An array of short-term loudness measurements sampled across the song in LUFS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/loudnessresult/integrated)*