# loudness

**Framework**: Music Understanding  
**Kind**: property  
**Role**: Instance Property

The aggregated loudness results, providing information about volume levels throughout the audio.

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
let loudness: LoudnessResult?
```

## See Also

### Getting music understanding session results
- [let instrumentActivity: InstrumentActivityResult?](./instrumentactivity.md)
  The aggregated instrument activity results, identifying which instruments are present and when they’re active.
- [let key: KeyResult?](./key.md)
  The aggregated key results, identifying the central note (tonic) and mode around which a piece of music is organized.
- [let pace: PaceResult?](./pace.md)
  The aggregated pace results, describing the energy and momentum variations over time.
- [let rhythm: RhythmResult?](./rhythm.md)
  The aggregated rhythm results, including detected beats, bars, and BPM.
- [let structure: StructureResult?](./structure.md)
  The aggregated structure results, identifying musical sections and their boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/sessionresult/loudness)*