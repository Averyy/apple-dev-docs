# readMicrophone(configuration:)

**Framework**: Create ML Components  
**Kind**: method

Reads an async sequence of audio frames captured with a microphone.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static func readMicrophone(configuration: AudioReader.Configuration = .init()) async throws -> AudioReader.MicrophoneAsyncBuffers
```

#### Return Value

An async sequence of `AVAudioPCMBuffer`.

## Parameters

- `configuration`: The configuration for reading buffers.

## See Also

- [static func read(contentsOf: URL, configuration: AudioReader.Configuration) throws -> AudioReader.AsyncBuffers](audioreader/read(contentsof:configuration:).md)
  Reads an audio file as an async sequence of audio buffers.
- [static read(_:configuration:)](audioreader/read(_:configuration:).md)
  Reads a sequence of annotated files as a lazy sequence of results each containing an audio buffers or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/readmicrophone(configuration:))*