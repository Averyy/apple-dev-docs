# beatsPerMinute

**Framework**: Music Understanding  
**Kind**: property

The tempo of the song in beats per minute.

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
let beatsPerMinute: Float?
```

#### Discussion

This value may be nil until enough audio has been analyzed.

## See Also

- [let bars: [CMTime]](rhythmresult/bars.md)
  The start time of each bar. A bar is a musical unit typically containing several beats.
- [let beats: [CMTime]](rhythmresult/beats.md)
  The timestamp of each detected beat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/rhythmresult/beatsperminute)*