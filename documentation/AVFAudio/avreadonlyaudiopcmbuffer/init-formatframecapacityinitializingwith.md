# init(format:frameCapacity:initializingWith:)

**Framework**: AVFAudio  
**Kind**: init

Creates a read-only buffer by allocating and initializing audio data via closure.

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
init(format: AVAudioFormat, frameCapacity: Int, initializingWith: (UnsafeMutablePointer<AudioBufferList>) throws -> Void) throws
```

#### Discussion

> **Note**: An error if allocation fails or the closure throws.

## Parameters

- `format`: The audio format for the buffer.
- `frameCapacity`: The capacity in audio frames.
- `initializingWith`: Closure that receives the mutable AudioBufferList to initialize.

## See Also

- [init(copying: AVAudioPCMBuffer)](avreadonlyaudiopcmbuffer/init(copying:).md)
  Creates a read-only buffer by copying audio data from an existing PCM buffer.
- [init(unsafeRetaining: sending AVAudioPCMBuffer)](avreadonlyaudiopcmbuffer/init(unsaferetaining:).md)
  Creates a read-only buffer by retaining the existing PCM buffer without copying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/init(format:framecapacity:initializingwith:))*