# AudioQueueProcessingTapNew(_:_:_:_:_:_:_:)

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
func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutableRawPointer?, _ inFlags: AudioQueueProcessingTapFlags, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus
```

## See Also

- [func AudioQueueProcessingTapGetQueueTime(AudioQueueProcessingTapRef, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueueprocessingtapgetqueuetime(_:_:_:).md)
- [func AudioQueueProcessingTapGetSourceAudio(AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audioqueueprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
- [func AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus](audioqueueprocessingtapdispose(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapnew(_:_:_:_:_:_:_:))*