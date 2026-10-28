# momentary

**Framework**: Music Understanding  
**Kind**: property  
**Role**: Instance Property

An array of momentary loudness measurements sampled across the song in LUFS.

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
let momentary: [MusicUnderstandingSession.TimedValue<Float>]
```

## Discussion

The measurement happens in 400 millisecond (ms) increments that advance 100ms at a time.

## See Also

### Getting loudness results
- [let integrated: MusicUnderstandingSession.TimedValue<Float>](./integrated.md)
  The integrated loudness of the song, measured in LUFS over its full duration.
- [let peak: MusicUnderstandingSession.TimedValue<Float>](./peak.md)
  The peak amplitude of the song in decibels (dB).
- [let shortTerm: [MusicUnderstandingSession.TimedValue<Float>]](./shortterm.md)
  An array of short-term loudness measurements sampled across the song in LUFS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/loudnessresult/momentary)*