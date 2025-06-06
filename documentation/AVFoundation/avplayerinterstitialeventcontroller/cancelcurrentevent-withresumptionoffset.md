# cancelCurrentEvent(withResumptionOffset:)

**Framework**: AVFoundation  
**Kind**: method

Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.

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
func cancelCurrentEvent(withResumptionOffset resumptionOffset: CMTime)
```

#### Discussion

When you cancel interstitial events using this method, the resumption offset value that you specify overrides the events’s [`resumptionOffset`](avplayerinterstitialevent/resumptionoffset.md) value.

> **Note**:  If you call this method during the handling of coinciding interstitial events, the system cancels all events for that time. Calling this method has no impact on schedule events that have dates or times later than this event.

 If you call this method during the handling of coinciding interstitial events, the system cancels all events for that time. Calling this method has no impact on schedule events that have dates or times later than this event.

## Parameters

- `resumptionOffset`: The time offset at which playback of the primary content resumes after interstitial playback finishes.

## See Also

- [var events: [AVPlayerInterstitialEvent]!](avplayerinterstitialeventcontroller/events.md)
  The current schedule of interstitial events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/cancelcurrentevent(withresumptionoffset:))*