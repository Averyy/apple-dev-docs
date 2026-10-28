# init(unsafeRetaining:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a read-only buffer by retaining the existing PCM buffer without copying.

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
init(unsafeRetaining buffer: sending AVAudioPCMBuffer)
```

## Discussion

> ⚠️ **Warning**: The caller must ensure the original buffer is not modified while this read-only buffer is in use. Violating this contract results in undefined behavior.

## Parameters

- `buffer`: The PCM buffer to retain (not copied).

## See Also

### Creating a read-only buffer
- [init(copying: AVAudioPCMBuffer)](./init%28copying%29.md)
  Creates a read-only buffer by copying audio data from an existing PCM buffer.
- [init(format: AVAudioFormat, frameCapacity: Int, initializingWith: (UnsafeMutablePointer<AudioBufferList>) throws -> Void) throws](./init%28format,framecapacity,initializingwith%29.md)
  Creates a read-only buffer by allocating and initializing audio data via closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/init(unsaferetaining:))*