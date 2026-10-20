# AudioQueueProcessingTapGetQueueTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioQueueProcessingTapGetQueueTime(AudioQueueProcessingTapRef inAQTap, Float64 *outQueueSampleTime, UInt32 *outQueueFrameCount);
```

## See Also

### Tapping the Queue’s Audio
- [func AudioQueueProcessingTapNew(AudioQueueRef, AudioQueueProcessingTapCallback, UnsafeMutableRawPointer?, AudioQueueProcessingTapFlags, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus](./audioqueueprocessingtapnew%28_,_,_,_,_,_,_%29.md)
- [func AudioQueueProcessingTapGetSourceAudio(AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./audioqueueprocessingtapgetsourceaudio%28_,_,_,_,_,_%29.md)
- [func AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus](./audioqueueprocessingtapdispose%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapgetqueuetime(_:_:_:))*