# segments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The segments for this snapshot.

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
var segments: [AVPlayerItemSegment] { get }
```

```objc
@property (readonly) NSArray<AVPlayerItemSegment *> * segments;
```

#### Discussion

The system presents segments in chronological order, contiguous from the previous element, and non-overlapping.

## See Also

### Inspecting the snapshot
- [var duration: CMTime](./duration.md)
  The total duration of the primary item and scheduled interstitial events.
- [var currentSegment: AVPlayerItemSegment?](./currentsegment.md)
  The currently playing segment.
- [class AVPlayerItemSegment](../avplayeritemsegment.md)
  An immutable object that represents a segment of time on the integrated timeline.
- [var currentTime: CMTime](./currenttime.md)
  The current time on the integrated timeline when the system created the snapshot.
- [var currentDate: Date?](./currentdate.md)
  The current date on the integrated timeline when the system created the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/segments)*