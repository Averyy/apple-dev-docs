# maxFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) CMTime maxFrameDuration;
```

## Discussion

This value is the reciprocal of [`minFrameRate`](./minframerate.md), and expresses the minimum frame rate as a duration.

## See Also

### Accessing properties
- [var maxFrameRate: Float64](./maxframerate.md)
  The maximum frame rate supported by the range.
- [var minFrameDuration: CMTime](./minframeduration.md)
  The minimum frame duration supported by the range.
- [var minFrameRate: Float64](./minframerate.md)
  The minimum frame rate supported by the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avframeraterange/maxframeduration)*