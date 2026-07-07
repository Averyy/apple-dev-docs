# withUnsafeAudioBufferList(_:)

**Framework**: AVFAudio  
**Kind**: method

Provides scoped read-only access to the audio buffer list.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func withUnsafeAudioBufferList<R>(_ body: (UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R
```

#### Return Value

The value returned by the closure.

#### Discussion

> ⚠️ **Warning**: Although the `AudioBufferList` pointer is const, each `AudioBuffer` within the list exposes `mData` as `UnsafeMutableRawPointer`. You must not modify the buffer data through these pointers. Doing so results in undefined behavior and violates the read-only contract of this type.

## Parameters

- `body`: A closure that receives a pointer to the audio buffer list.

## See Also

- [func channelData(Int) -> AVReadOnlyAudioPCMBuffer.ChannelData](avreadonlyaudiopcmbuffer/channeldata(_:).md)
  Returns read-only access to a specific channel’s data.
- [AVReadOnlyAudioPCMBuffer.ChannelData](avreadonlyaudiopcmbuffer/channeldata.md)
  Represents read-only channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/withunsafeaudiobufferlist(_:))*