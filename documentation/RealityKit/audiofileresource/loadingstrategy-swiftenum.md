# AudioFileResource.LoadingStrategy

**Framework**: RealityKit  
**Kind**: enum

A container for different strategies on how to handle resources’ data before and during playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
enum LoadingStrategy
```

## Topics

### Specifying a loading strategy
- [AudioFileResource.LoadingStrategy.preload](audiofileresource/loadingstrategy-swift.enum/preload.md)
  Load and decode all the data into memory before playback.
- [AudioFileResource.LoadingStrategy.stream](audiofileresource/loadingstrategy-swift.enum/stream.md)
  Stream data from disk, decoding in real time.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AudioFileResource.Configuration](audiofileresource/configuration-swift.struct.md)
  A container for various settings for loading an audio file resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/loadingstrategy-swift.enum)*