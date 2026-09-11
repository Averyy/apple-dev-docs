# peak

**Framework**: Music Understanding  
**Kind**: property

The peak amplitude of the song in decibels (dB).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
let peak: MusicUnderstandingSession.TimedValue<Float>
```

## See Also

- [let integrated: MusicUnderstandingSession.TimedValue<Float>](loudnessresult/integrated.md)
  The integrated loudness of the song, measured in LUFS over its full duration.
- [let momentary: [MusicUnderstandingSession.TimedValue<Float>]](loudnessresult/momentary.md)
  An array of momentary loudness measurements sampled across the song in LUFS.
- [let shortTerm: [MusicUnderstandingSession.TimedValue<Float>]](loudnessresult/shortterm.md)
  An array of short-term loudness measurements sampled across the song in LUFS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/loudnessresult/peak)*