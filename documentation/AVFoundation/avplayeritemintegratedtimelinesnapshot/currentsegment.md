# currentSegment

**Framework**: AVFoundation  
**Kind**: property

The currently playing segment.

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
var currentSegment: AVPlayerItemSegment? { get }
```

## See Also

- [var duration: CMTime](avplayeritemintegratedtimelinesnapshot/duration.md)
  The total duration of the primary item and scheduled interstitial events.
- [var segments: [AVPlayerItemSegment]](avplayeritemintegratedtimelinesnapshot/segments.md)
  The segments for this snapshot.
- [class AVPlayerItemSegment](avplayeritemsegment.md)
  An immutable object that represents a segment of time on the integrated timeline.
- [var currentTime: CMTime](avplayeritemintegratedtimelinesnapshot/currenttime.md)
  The current time on the integrated timeline when the system created the snapshot.
- [var currentDate: Date?](avplayeritemintegratedtimelinesnapshot/currentdate.md)
  The current date on the integrated timeline when the system created the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentsegment)*