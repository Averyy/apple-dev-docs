# beatsPerMinute

**Framework**: Music Understanding  
**Kind**: property

The tempo of the song in beats per minute.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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