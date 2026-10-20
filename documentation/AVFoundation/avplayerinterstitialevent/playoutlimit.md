# playoutLimit

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time offset at which playback of the interstitial ends.

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
var playoutLimit: CMTime { get set }
```

```objc
@property (nonatomic, readonly) CMTime playoutLimit;
```

#### Discussion

This value can be any positive numeric value, or [`invalid`](../../CoreMedia/cmtime/invalid.md) (the default) which indicates no limit.

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
- [var alignsStartWithPrimarySegmentBoundary: Bool](./alignsstartwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [var alignsResumptionWithPrimarySegmentBoundary: Bool](./alignsresumptionwithprimarysegmentboundary.md)
  A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/playoutlimit)*