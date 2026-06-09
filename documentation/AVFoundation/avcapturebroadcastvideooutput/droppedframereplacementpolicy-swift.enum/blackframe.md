# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.blackFrame

**Framework**: AVFoundation  
**Kind**: case

Insert a black frame as replacement. When a frame is dropped, a black frame is inserted at the expected presentation time. This maintains output timing continuity while providing a clear visual indication of the dropped frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
case blackFrame
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/blackframe)*