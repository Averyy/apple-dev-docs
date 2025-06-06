# maxFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The maximum frame duration supported by the range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var maxFrameDuration: CMTime { get }
```

#### Discussion

This value is the reciprocal of [`minFrameRate`](avframeraterange/minframerate.md), and expresses the minimum frame rate as a duration.

## See Also

- [var maxFrameRate: Float64](avframeraterange/maxframerate.md)
  The maximum frame rate supported by the range.
- [var minFrameDuration: CMTime](avframeraterange/minframeduration.md)
  The minimum frame duration supported by the range.
- [var minFrameRate: Float64](avframeraterange/minframerate.md)
  The minimum frame rate supported by the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avframeraterange/maxframeduration)*