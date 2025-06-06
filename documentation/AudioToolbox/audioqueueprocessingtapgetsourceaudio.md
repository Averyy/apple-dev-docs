# AudioQueueProcessingTapGetSourceAudio(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTapRef, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outFlags: UnsafeMutablePointer<AudioQueueProcessingTapFlags>, _ outNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus
```

## See Also

- [func AudioQueueProcessingTapNew(AudioQueueRef, AudioQueueProcessingTapCallback, UnsafeMutableRawPointer?, AudioQueueProcessingTapFlags, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus](audioqueueprocessingtapnew(_:_:_:_:_:_:_:).md)
- [func AudioQueueProcessingTapGetQueueTime(AudioQueueProcessingTapRef, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueueprocessingtapgetqueuetime(_:_:_:).md)
- [func AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus](audioqueueprocessingtapdispose(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapgetsourceaudio(_:_:_:_:_:_:))*