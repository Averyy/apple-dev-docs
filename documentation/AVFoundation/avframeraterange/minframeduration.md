# minFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The minimum frame duration supported by the range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var minFrameDuration: CMTime { get }
```

#### Discussion

This value is the reciprocal of [`maxFrameRate`](avframeraterange/maxframerate.md), and expresses the maximum frame rate as a duration.

## See Also

- [var maxFrameDuration: CMTime](avframeraterange/maxframeduration.md)
  The maximum frame duration supported by the range.
- [var maxFrameRate: Float64](avframeraterange/maxframerate.md)
  The maximum frame rate supported by the range.
- [var minFrameRate: Float64](avframeraterange/minframerate.md)
  The minimum frame rate supported by the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avframeraterange/minframeduration)*