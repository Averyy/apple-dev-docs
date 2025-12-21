# read(contentsOf:configuration:)

**Framework**: Create ML Components  
**Kind**: method

Reads an audio file as an async sequence of audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func read(contentsOf url: URL, configuration: AudioReader.Configuration = .init()) throws -> AudioReader.AsyncBuffers
```

#### Return Value

An async sequence of `AVAudioPCMBuffer`.

## Parameters

- `url`: An audio file URL.
- `configuration`: The configuration for reading buffers.

## See Also

- [static read(_:configuration:)](audioreader/read(_:configuration:).md)
  Reads a sequence of annotated files as a lazy sequence of results each containing an audio buffers or an error.
- [static func readMicrophone(configuration: AudioReader.Configuration) async throws -> AudioReader.MicrophoneAsyncBuffers](audioreader/readmicrophone(configuration:).md)
  Reads an async sequence of audio frames captured with a microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/read(contentsof:configuration:))*