# duration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CMTime duration;
```

#### Discussion

The duration property takes into account the interstitial event’s [`playoutLimit`](../avplayerinterstitialevent/playoutlimit.md) and [`resumptionOffset`](../avplayerinterstitialevent/resumptionoffset.md) values.

Before loading the duration of the primary item, the value of this property is [`invalid`](../../CoreMedia/cmtime/invalid.md). For livestreams, this value is [`indefinite`](../../CoreMedia/cmtime/indefinite.md).

## See Also

### Inspecting the snapshot
- [var currentSegment: AVPlayerItemSegment?](./currentsegment.md)
  The currently playing segment.
- [var segments: [AVPlayerItemSegment]](./segments.md)
  The segments for this snapshot.
- [class AVPlayerItemSegment](../avplayeritemsegment.md)
  An immutable object that represents a segment of time on the integrated timeline.
- [var currentTime: CMTime](./currenttime.md)
  The current time on the integrated timeline when the system created the snapshot.
- [var currentDate: Date?](./currentdate.md)
  The current date on the integrated timeline when the system created the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/duration)*