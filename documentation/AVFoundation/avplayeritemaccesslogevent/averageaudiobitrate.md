# averageAudioBitrate

**Framework**: AVFoundation  
**Kind**: property

The audio track’s average bit rate, in bits per second.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var averageAudioBitrate: Double { get }
```

#### Discussion

The property corresponds to “c-avg-audio-bitrate”.

This property returns a non-positive value if unknown.

This property is not compatible with key-value observing.

## See Also

- [var observedBitrateStandardDeviation: Double](avplayeritemaccesslogevent/observedbitratestandarddeviation.md)
  The standard deviation of the observed segment download bit rates.
- [var observedMaxBitrate: Double](avplayeritemaccesslogevent/observedmaxbitrate.md)
  The maximum observed segment download bit rate.
- [var observedMinBitrate: Double](avplayeritemaccesslogevent/observedminbitrate.md)
  The minimum observed segment download bit rate.
- [var switchBitrate: Double](avplayeritemaccesslogevent/switchbitrate.md)
  The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [var indicatedBitrate: Double](avplayeritemaccesslogevent/indicatedbitrate.md)
  The throughput, in bits per second, required to play the stream, as advertised by the server.
- [var observedBitrate: Double](avplayeritemaccesslogevent/observedbitrate.md)
  The empirical throughput, in bits per second, across all media downloaded.
- [var averageVideoBitrate: Double](avplayeritemaccesslogevent/averagevideobitrate.md)
  The video track’s average bit rate, in bits per second.
- [var indicatedAverageBitrate: Double](avplayeritemaccesslogevent/indicatedaveragebitrate.md)
  The average throughput, in bits per second, required to play the stream, as advertised by the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/averageaudiobitrate)*