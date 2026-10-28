# init(format:frameCapacity:initializingWith:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a read-only buffer by allocating and initializing audio data via closure.

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
init(format: AVAudioFormat, frameCapacity: Int, initializingWith: (UnsafeMutablePointer<AudioBufferList>) throws -> Void) throws
```

## Discussion

> **Throws**: An error if allocation fails or the closure throws.

## Parameters

- `format`: The audio format for the buffer.
- `frameCapacity`: The capacity in audio frames.
- `initializingWith`: Closure that receives the mutable AudioBufferList to initialize.

## See Also

### Creating a read-only buffer
- [init(copying: AVAudioPCMBuffer)](./init%28copying%29.md)
  Creates a read-only buffer by copying audio data from an existing PCM buffer.
- [init(unsafeRetaining: sending AVAudioPCMBuffer)](./init%28unsaferetaining%29.md)
  Creates a read-only buffer by retaining the existing PCM buffer without copying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/init(format:framecapacity:initializingwith:))*