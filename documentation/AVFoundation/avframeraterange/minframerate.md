# minFrameRate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The minimum frame rate supported by the range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var minFrameRate: Float64 { get }
```

```objc
@property (readonly) Float64 minFrameRate;
```

#### Discussion

The frame is given in frames per second.

## See Also

### Accessing properties
- [var maxFrameDuration: CMTime](./maxframeduration.md)
  The maximum frame duration supported by the range.
- [var maxFrameRate: Float64](./maxframerate.md)
  The maximum frame rate supported by the range.
- [var minFrameDuration: CMTime](./minframeduration.md)
  The minimum frame duration supported by the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avframeraterange/minframerate)*