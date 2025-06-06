# customVideoCompositor

**Framework**: AVFoundation  
**Kind**: property

A custom video compositor for the output.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var customVideoCompositor: (any AVVideoCompositing)? { get }
```

#### Discussion

This property is `nil` if there isn’t a custom video compositor, or if the internal video compositor is in use.

## See Also

- [var videoComposition: AVVideoComposition?](avassetreadervideocompositionoutput/videocomposition.md)
  The video composition to use for the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/customvideocompositor)*