# observedMaxBitrate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The maximum observed segment download bit rate.

**Availability**:
- iOS 7.0+ - Deprecated in 15.0
- iPadOS 7.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.9+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- watchOS 1.0+ - Deprecated in 8.0

> **Deprecated**: Use observedBitrateStandardDeviation to monitor variance in network bitrate.

## Declaration

```swift
var observedMaxBitrate: Double { get }
```

```objc
@property (nonatomic, readonly) double observedMaxBitrate;
```

#### Discussion

The value of the property is negative if unknown.

Corresponds to “c-observed-max-bitrate”.

This property is not compatible with key-value observing.

## See Also

### Getting bit rate log events
- [var observedBitrateStandardDeviation: Double](./observedbitratestandarddeviation.md)
  The standard deviation of the observed segment download bit rates.
- [var observedMinBitrate: Double](./observedminbitrate.md)
  The minimum observed segment download bit rate.
- [var switchBitrate: Double](./switchbitrate.md)
  The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [var indicatedBitrate: Double](./indicatedbitrate.md)
  The throughput, in bits per second, required to play the stream, as advertised by the server.
- [var observedBitrate: Double](./observedbitrate.md)
  The empirical throughput, in bits per second, across all media downloaded.
- [var averageAudioBitrate: Double](./averageaudiobitrate.md)
  The audio track’s average bit rate, in bits per second.
- [var averageVideoBitrate: Double](./averagevideobitrate.md)
  The video track’s average bit rate, in bits per second.
- [var indicatedAverageBitrate: Double](./indicatedaveragebitrate.md)
  The average throughput, in bits per second, required to play the stream, as advertised by the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/observedmaxbitrate)*