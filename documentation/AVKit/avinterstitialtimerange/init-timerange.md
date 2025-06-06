# init(timeRange:)

**Framework**: AVKit  
**Kind**: init

Initializes an interstitial time range object with the specified time range.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
init(timeRange: CMTimeRange)
```

#### Return Value

A new interstitial time range object.

#### Discussion

To associate interstitial time ranges with an asset for playback, use the [`interstitialTimeRanges`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/interstitialTimeRanges) property of an [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) object.

## Parameters

- `timeRange`: The time range to designate as interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterstitialtimerange/init(timerange:))*