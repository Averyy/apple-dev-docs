# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.repeatPreviousFrame

**Framework**: AVFoundation  
**Kind**: case

Repeat the previous frame as replacement. When a frame is dropped, the most recent successfully output frame is repeated at the expected presentation time. This is the default behavior and provides smoother visual continuity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
case repeatPreviousFrame
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/repeatpreviousframe)*