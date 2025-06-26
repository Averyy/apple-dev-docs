# duration

**Framework**: AVFoundation  
**Kind**: property

The total duration of the primary item and scheduled interstitial events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var duration: CMTime { get }
```

#### Discussion

The duration property takes into account the interstitial event’s [`playoutLimit`](avplayerinterstitialevent/playoutlimit.md) and [`resumptionOffset`](avplayerinterstitialevent/resumptionoffset.md) values.

Before loading the duration of the primary item, the value of this property is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid). For livestreams, this value is [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite).

## See Also

- [var currentSegment: AVPlayerItemSegment?](avplayeritemintegratedtimelinesnapshot/currentsegment.md)
  The currently playing segment.
- [var segments: [AVPlayerItemSegment]](avplayeritemintegratedtimelinesnapshot/segments.md)
  The segments for this snapshot.
- [class AVPlayerItemSegment](avplayeritemsegment.md)
  An immutable object that represents a segment of time on the integrated timeline.
- [var currentTime: CMTime](avplayeritemintegratedtimelinesnapshot/currenttime.md)
  The current time on the integrated timeline when the system created the snapshot.
- [var currentDate: Date?](avplayeritemintegratedtimelinesnapshot/currentdate.md)
  The current date on the integrated timeline when the system created the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/duration)*