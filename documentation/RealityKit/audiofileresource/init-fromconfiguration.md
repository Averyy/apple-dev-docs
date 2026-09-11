# init(from:configuration:)

**Framework**: RealityKit  
**Kind**: init

Initializes an AudioFileResource from in-memory data asynchronously.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from data: Data, configuration: AudioFileResource.Configuration = .init()) async throws
```

#### Discussion

This API creates a memory-resident audio resource that never writes to disk. The data must contain a valid audio file format (WAV, M4A, etc.).

> **Note**: `AudioFileResource.Error` if the data is invalid or cannot be processed

## Parameters

- `data`: The audio file data in memory
- `configuration`: Configuration settings for the audio resource


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/init(from:configuration:))*