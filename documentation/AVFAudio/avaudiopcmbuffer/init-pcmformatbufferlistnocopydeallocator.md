# init(pcmFormat:bufferListNoCopy:deallocator:)

**Framework**: AVFAudio  
**Kind**: init

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

#### Return Value

A new [`AVAudioPCMBuffer`](avaudiopcmbuffer.md) instance, or `nil` if it’s not possible.

#### Discussion

Use the deallocator parameter to define your own deallocation behavior for the audio buffer list’s underlying memory. The buffer list sent to the deallocator is identical to the one you specify, in term of buffer count and each buffer’s [`mData`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBuffer/mData) and [`mDataByteSize`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBuffer/mDataByteSize) members.

The method returns `nil` due to the following reasons:

- The format has zero bytes per frame.
- The buffer you specify has zero number of buffers.
- The buffer list’s pointer to the buffer of audio data is in a `nil` state.
- Each of the buffer’s data byte size aren’t equal, or if any of the buffers’ data byte size is zero.
- There’s a mismatch between the format’s number of buffers and the buffer list’s size (1 if interleaved, [`mChannelsPerFrame`](https://developer.apple.com/documentation/CoreAudioTypes/AudioStreamBasicDescription/mChannelsPerFrame) if deinterleaved).

## Parameters

- `format`: The format of the PCM audio the buffer contains.
- `bufferList`: The buffer list with the memory to contain the PCM audio data.
- `deallocator`: The closure the method invokes when the resulting PCM buffer object deallocates.

## See Also

- [init?(pcmFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](avaudiopcmbuffer/init(pcmformat:framecapacity:).md)
  Creates a PCM audio buffer instance for PCM audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:))*