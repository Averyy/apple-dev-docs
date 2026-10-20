# segments

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time mappings from the track’s media samples to its timeline.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var segments: [AVCompositionTrackSegment] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<AVCompositionTrackSegment *> * segments;
```

## See Also

### Accessing track segments
- [func segment(forTrackTime: CMTime) -> AVCompositionTrackSegment?](./segment%28fortracktime%29.md)
  Returns a segment whose target time range contains, or is closest to, the specified track time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/segments)*