# channelData(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Returns read-only access to a specific channel’s data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func channelData(_ index: Int) -> AVAudioPCMBuffer.ChannelData
```

## Return Value

A `ChannelData` enum containing the channel’s sample data.

## Discussion

The returned `ChannelData` is tied to the lifetime of this buffer and provides type-safe read-only access to the channel’s sample data.

- Example:

> ⚠️ **Warning**: This function cannot enforce exclusivity at compile time because `AVAudioPCMBuffer` is an Objective-C class. The caller must ensure proper synchronization when accessing the buffer concurrently or when the buffer might be modified.

> **Note**: Provides access to valid data only (up to `frameLength`).

```swift
for channelIndex in 0..<Int(buffer.format.channelCount) {
    let channelData = buffer.channelData(channelIndex)
    switch channelData {
    case .float(let samples):
        // Read Float32 data
        for frame in 0..<samples.count {
            let value = samples[frame]
        }
    case .int16(let samples):
        // Read Int16 data
    case .int32(let samples):
        // Read Int32 data
    }
}
```

## Parameters

- `index`: The zero-based channel index.

## See Also

### Accessing PCM buffer data
- [func mutableChannelData(Int) -> AVAudioPCMBuffer.MutableChannelData](./mutablechanneldata%28_%29.md)
  Returns mutable access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](./withunsafeaudiobufferlist%28_%29.md)
  Provides scoped read-only access to the audio buffer list.
- [var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>?](./floatchanneldata.md)
  The buffer’s audio samples as floating point values.
- [var frameCapacity: AVAudioFrameCount](./framecapacity.md)
  The buffer’s capacity, in audio sample frames.
- [var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>?](./int16channeldata.md)
  The buffer’s 16-bit integer audio samples.
- [var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>?](./int32channeldata.md)
  The buffer’s 32-bit integer audio samples.
- [var stride: Int](./stride.md)
  The buffer’s number of interleaved channels.
- [AVAudioPCMBuffer.ChannelData](./channeldata.md)
  Represents read-only channel data.
- [AVAudioPCMBuffer.MutableChannelData](./mutablechanneldata.md)
  Represents mutable channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/channeldata(_:))*