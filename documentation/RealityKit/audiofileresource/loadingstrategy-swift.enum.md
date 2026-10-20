# AudioFileResource.LoadingStrategy

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

A container for different strategies on how to handle resources’ data before and during playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
enum LoadingStrategy
```

## Topics

### Specifying a loading strategy
- [AudioFileResource.LoadingStrategy.preload](./loadingstrategy-swift.enum/preload.md)
  Load and decode all the data into memory before playback.
- [AudioFileResource.LoadingStrategy.stream](./loadingstrategy-swift.enum/stream.md)
  Stream data from disk, decoding in real time.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AudioFileResource.Configuration](./configuration-swift.struct.md)
  A container for various settings for loading an audio file resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/loadingstrategy-swift.enum)*