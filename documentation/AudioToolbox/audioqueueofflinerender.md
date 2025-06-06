# AudioQueueOfflineRender(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Exports audio to a buffer, instead of to a device, using a playback audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueOfflineRender(_ inAQ: AudioQueueRef, _ inTimestamp: UnsafePointer<AudioTimeStamp>, _ ioBuffer: AudioQueueBufferRef, _ inNumberFrames: UInt32) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

When you change a playback audio queue’s rendering mode to offline, using the [`AudioQueueSetOfflineRenderFormat(_:_:_:)`](audioqueuesetofflinerenderformat(_:_:_:).md) function, you gain access to the rendered audio. You can then write the audio to a file, rather than have it play to external hardware such as a loudspeaker.

## Parameters

- `inAQ`: The playback audio queue.
- `inTimestamp`: The time corresponding to the beginning of the current audio queue buffer. This function uses the   field of the   data structure.
- `ioBuffer`: On input, a buffer you supply to hold rendered audio data. On output, the rendered audio data, which you can then write to a file.
- `inNumberFrames`: The number of frames of audio to render.

## See Also

- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueueSetOfflineRenderFormat(AudioQueueRef, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioChannelLayout>?) -> OSStatus](audioqueuesetofflinerenderformat(_:_:_:).md)
  Sets the rendering mode and audio format for a playback audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueofflinerender(_:_:_:_:))*