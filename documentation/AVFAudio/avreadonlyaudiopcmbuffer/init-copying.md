# init(copying:)

**Framework**: AVFAudio  
**Kind**: init

Creates a read-only buffer by copying audio data from an existing PCM buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(copying buffer: AVAudioPCMBuffer)
```

#### Discussion

This initializer creates a new `AVAudioPCMBuffer` and copies all audio data, ensuring the original buffer can continue to be used safely.

## Parameters

- `buffer`: The source PCM buffer to copy from.

## See Also

- [init(format: AVAudioFormat, frameCapacity: Int, initializingWith: (UnsafeMutablePointer<AudioBufferList>) throws -> Void) throws](avreadonlyaudiopcmbuffer/init(format:framecapacity:initializingwith:).md)
  Creates a read-only buffer by allocating and initializing audio data via closure.
- [init(unsafeRetaining: sending AVAudioPCMBuffer)](avreadonlyaudiopcmbuffer/init(unsaferetaining:).md)
  Creates a read-only buffer by retaining the existing PCM buffer without copying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/init(copying:))*