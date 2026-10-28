# mutableChannelData(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Returns mutable access to a specific channel’s data.

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
func mutableChannelData(_ index: Int) -> AVAudioPCMBuffer.MutableChannelData
```

## Return Value

A `MutableChannelData` enum containing the channel’s sample data.

## Discussion

The returned `MutableChannelData` is tied to the lifetime of this buffer and provides type-safe mutable access to the channel’s sample data.

- Example:

> ⚠️ **Warning**: This function cannot enforce exclusivity at compile time because `AVAudioPCMBuffer` is an Objective-C class. The caller must ensure they don’t create overlapping mutable views to the same memory. It is safe to access different channels simultaneously or different regions of the same channel.

> **Note**: Provides access to the entire buffer (up to `frameCapacity`). frameLength needs to be updated if the size changes.

```swift
for channelIndex in 0..<Int(buffer.format.channelCount) {
    switch buffer.mutableChannelData(channelIndex) {
    case .float(var samples):
        // Modify Float32 data
        for frame in 0..<samples.count {
            samples[frame] = 0.0
        }
    case .int16(var samples):
        // Modify Int16 data
    case .int32(var samples):
        // Modify Int32 data
    }
}
```

## Parameters

- `index`: The zero-based channel index.

## See Also

### Accessing PCM buffer data
- [func channelData(Int) -> AVAudioPCMBuffer.ChannelData](./channeldata%28_%29.md)
  Returns read-only access to a specific channel’s data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/mutablechanneldata(_:))*