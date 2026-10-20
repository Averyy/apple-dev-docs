# alignsStartWithPrimarySegmentBoundary

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var alignsStartWithPrimarySegmentBoundary: Bool { get set }
```

```objc
@property (nonatomic, readonly) BOOL alignsStartWithPrimarySegmentBoundary;
```

#### Discussion

If the value is [`true`](../../Swift/true.md), the system adjusts the start time or date of the interstitial to the nearest segment boundary when the primary player is playing an HTTP Live Streaming asset.

## See Also

### Inspecting timing
- [var time: CMTime](./time.md)
  A time within the timeline of the primary content that playback of interstitial content begins.
- [var date: Date?](./date.md)
  A date within the date range of the primary content that playback of interstitial content begins.
- [var willPlayOnce: Bool](./willplayonce.md)
  A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [var resumptionOffset: CMTime](./resumptionoffset.md)
  A time offset at which playback of primary content resumes after interstitial content finishes.
- [var playoutLimit: CMTime](./playoutlimit.md)
  The time offset at which playback of the interstitial ends.
- [var alignsResumptionWithPrimarySegmentBoundary: Bool](./alignsresumptionwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/alignsstartwithprimarysegmentboundary)*