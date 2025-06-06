# resumptionOffset

**Framework**: AVFoundation  
**Kind**: property

A time offset at which playback of primary content resumes after interstitial content finishes.

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
var resumptionOffset: CMTime { get set }
```

#### Discussion

This property supports definite time values. Specify [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite) to indicate that the effective resumption time offset should align with the clock time elapsed during interstitial playback; this value is typically suitable for live broadcasts.

The default value is [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero).

## See Also

- [var time: CMTime](avplayerinterstitialevent/time.md)
  A time within the timeline of the primary content that playback of interstitial content begins.
- [var date: Date?](avplayerinterstitialevent/date.md)
  A date within the date range of the primary content that playback of interstitial content begins.
- [var willPlayOnce: Bool](avplayerinterstitialevent/willplayonce.md)
  A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [var playoutLimit: CMTime](avplayerinterstitialevent/playoutlimit.md)
  The time offset at which playback of the interstitial ends.
- [var alignsStartWithPrimarySegmentBoundary: Bool](avplayerinterstitialevent/alignsstartwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [var alignsResumptionWithPrimarySegmentBoundary: Bool](avplayerinterstitialevent/alignsresumptionwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/resumptionoffset)*