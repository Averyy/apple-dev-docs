# indicatedBitrate

**Framework**: AVFoundation  
**Kind**: property

The throughput, in bits per second, required to play the stream, as advertised by the server.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var indicatedBitrate: Double { get }
```

#### Discussion

The property corresponds to “sc-indicated-bitrate”.

The value of this property is negative if unknown.

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
- [var observedBitrate: Double](avplayeritemaccesslogevent/observedbitrate.md)
  The empirical throughput, in bits per second, across all media downloaded.
- [var averageAudioBitrate: Double](avplayeritemaccesslogevent/averageaudiobitrate.md)
  The audio track’s average bit rate, in bits per second.
- [var averageVideoBitrate: Double](avplayeritemaccesslogevent/averagevideobitrate.md)
  The video track’s average bit rate, in bits per second.
- [var indicatedAverageBitrate: Double](avplayeritemaccesslogevent/indicatedaveragebitrate.md)
  The average throughput, in bits per second, required to play the stream, as advertised by the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/indicatedbitrate)*