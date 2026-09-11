# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.blackFrame

**Framework**: AVFoundation  
**Kind**: case

Insert a black frame as replacement. When a frame is dropped, a black frame is inserted at the expected presentation time. This maintains output timing continuity while providing a clear visual indication of the dropped frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
case blackFrame
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/blackframe)*