# AudioQueueProcessingTapGetQueueTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueProcessingTapGetQueueTime(_ inAQTap: AudioQueueProcessingTapRef, _ outQueueSampleTime: UnsafeMutablePointer<Float64>, _ outQueueFrameCount: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioQueueProcessingTapNew(AudioQueueRef, AudioQueueProcessingTapCallback, UnsafeMutableRawPointer?, AudioQueueProcessingTapFlags, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus](audioqueueprocessingtapnew(_:_:_:_:_:_:_:).md)
- [func AudioQueueProcessingTapGetSourceAudio(AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audioqueueprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
- [func AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus](audioqueueprocessingtapdispose(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapgetqueuetime(_:_:_:))*