# timeRange

**Framework**: AVFoundation  
**Kind**: property

The time range of the media timeline in which the captions must exist.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

#### Discussion

If captions need to appear only after the start of the associated media, the start time of this time range can be less than the start time of the first caption’s time range.

If the media duration is unknown, this time range can have a duration of [`positiveInfinity`](https://developer.apple.com/documentation/CoreMedia/CMTime/positiveInfinity). However, to comprehensively validate the conversion of closed captions, set the duration of the time range to the duration of the associated media.

## See Also

- [var captions: [AVCaption]](avcaptionconversionvalidator/captions.md)
  The array of captions that the system validates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/timerange)*