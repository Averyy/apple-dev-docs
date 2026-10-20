# init(pcmFormat:bufferListNoCopy:deallocator:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a PCM audio buffer instance without copying samples, for PCM audio data, with a specified buffer list and a deallocator closure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init?(pcmFormat format: AVAudioFormat, bufferListNoCopy bufferList: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)? = nil)
```

```objc
- (instancetype) initWithPCMFormat:(AVAudioFormat *) format bufferListNoCopy:(const AudioBufferList *) bufferList deallocator:(void (^)(const AudioBufferList *)) deallocator;
```

#### Return Value

A new [`AVAudioPCMBuffer`](../avaudiopcmbuffer.md) instance, or `nil` if it’s not possible.

#### Discussion

Use the deallocator parameter to define your own deallocation behavior for the audio buffer list’s underlying memory. The buffer list sent to the deallocator is identical to the one you specify, in term of buffer count and each buffer’s [`mData`](../../CoreAudioTypes/audiobuffer/mdata.md) and [`mDataByteSize`](../../CoreAudioTypes/audiobuffer/mdatabytesize.md) members.

The method returns `nil` due to the following reasons:

- The format has zero bytes per frame.
- The buffer you specify has zero number of buffers.
- The buffer list’s pointer to the buffer of audio data is in a `nil` state.
- Each of the buffer’s data byte size aren’t equal, or if any of the buffers’ data byte size is zero.
- There’s a mismatch between the format’s number of buffers and the buffer list’s size (1 if interleaved, [`mChannelsPerFrame`](../../CoreAudioTypes/audiostreambasicdescription/mchannelsperframe.md) if deinterleaved).

## Parameters

- `format`: The format of the PCM audio the buffer contains.
- `bufferList`: The buffer list with the memory to contain the PCM audio data.
- `deallocator`: The closure the method invokes when the resulting PCM buffer object deallocates.

## See Also

### Creating a PCM audio buffer
- [init?(pcmFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](./init%28pcmformat,framecapacity%29-5jhd5.md)
  Creates a PCM audio buffer instance for PCM audio data.
- [convenience init(copying: AVAudioPCMBuffer)](./init%28copying%29-68es5.md)
  Creates a mutable buffer by copying another PCM buffer’s audio data.
- [convenience init(copying: AVReadOnlyAudioPCMBuffer)](./init%28copying%29-875xm.md)
  Creates a mutable buffer by copying a read-only buffer’s audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:)-9iwe7)*