# predictedCurrentMatchOffset

**Framework**: ShazamKit  
**Kind**: property

The updated timecode in the reference recording that matches the current playback position of the query audio, in seconds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var predictedCurrentMatchOffset: TimeInterval { get }
```

## Mentions

- [Matching audio using the built-in microphone](matching-audio-using-the-built-in-microphone.md)

## See Also

- [var matchOffset: TimeInterval](shmatchedmediaitem/matchoffset.md)
  The timecode in the reference recording that matches the start of the query, in seconds.
- [var frequencySkew: Float](shmatchedmediaitem/frequencyskew.md)
  A multiple for the difference in frequency between the matched audio and the query audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmatchedmediaitem/predictedcurrentmatchoffset)*