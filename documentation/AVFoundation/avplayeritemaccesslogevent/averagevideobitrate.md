# averageVideoBitrate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video track’s average bit rate, in bits per second.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var averageVideoBitrate: Double { get }
```

```objc
@property (nonatomic, readonly) double averageVideoBitrate;
```

#### Discussion

The property corresponds to “c-avg-video-bitrate”.

This property returns the average bitrate of the video track if it is unmuxed, or the average bitrate of the combined content if muxed. Measured in bits per second.

The value is negative if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting bit rate log events
- [var observedBitrateStandardDeviation: Double](./observedbitratestandarddeviation.md)
  The standard deviation of the observed segment download bit rates.
- [var observedMaxBitrate: Double](./observedmaxbitrate.md)
  The maximum observed segment download bit rate.
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
- [var indicatedAverageBitrate: Double](./indicatedaveragebitrate.md)
  The average throughput, in bits per second, required to play the stream, as advertised by the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/averagevideobitrate)*