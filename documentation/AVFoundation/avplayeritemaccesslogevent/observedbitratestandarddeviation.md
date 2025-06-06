# observedBitrateStandardDeviation

**Framework**: AVFoundation  
**Kind**: property

The standard deviation of the observed segment download bit rates.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var observedBitrateStandardDeviation: Double { get }
```

#### Discussion

The value of the property is negative if unknown.

Corresponds to “c-observed-bitrate-sd”.

This property is not compatible with key-value observing.

## See Also

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
- [var averageAudioBitrate: Double](avplayeritemaccesslogevent/averageaudiobitrate.md)
  The audio track’s average bit rate, in bits per second.
- [var averageVideoBitrate: Double](avplayeritemaccesslogevent/averagevideobitrate.md)
  The video track’s average bit rate, in bits per second.
- [var indicatedAverageBitrate: Double](avplayeritemaccesslogevent/indicatedaveragebitrate.md)
  The average throughput, in bits per second, required to play the stream, as advertised by the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/observedbitratestandarddeviation)*