# rhythm

**Framework**: Music Understanding  
**Kind**: property

The aggregated rhythm results, including detected beats, bars, and BPM.

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
let rhythm: RhythmResult?
```

## See Also

- [let instrumentActivity: InstrumentActivityResult?](musicunderstandingsession/sessionresult/instrumentactivity.md)
  The aggregated instrument activity results, identifying which instruments are present and when they’re active.
- [let key: KeyResult?](musicunderstandingsession/sessionresult/key.md)
  The aggregated key results, identifying the central note (tonic) and mode around which a piece of music is organized.
- [let loudness: LoudnessResult?](musicunderstandingsession/sessionresult/loudness.md)
  The aggregated loudness results, providing information about volume levels throughout the audio.
- [let pace: PaceResult?](musicunderstandingsession/sessionresult/pace.md)
  The aggregated pace results, describing the energy and momentum variations over time.
- [let structure: StructureResult?](musicunderstandingsession/sessionresult/structure.md)
  The aggregated structure results, identifying musical sections and their boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/sessionresult/rhythm)*