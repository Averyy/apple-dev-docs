# loadAsync(named:in:inputMode:loadingStrategy:shouldLoop:)

**Framework**: RealityKit  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(named name: String, in bundle: Bundle? = nil, inputMode: AudioResource.InputMode = .spatial, loadingStrategy: AudioFileResource.LoadingStrategy = .preload, shouldLoop: Bool = false) -> LoadRequest<AudioFileResource>
```

## See Also

- [static func load(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](audiofileresource/load(named:in:inputmode:loadingstrategy:shouldloop:).md)
  Synchronously loads an audio resource.
- [static func load(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](audiofileresource/load(contentsof:withname:inputmode:loadingstrategy:shouldloop:).md)
  Synchronously loads an audio resource.
- [static func loadAsync(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](audiofileresource/loadasync(contentsof:withname:inputmode:loadingstrategy:shouldloop:).md)
- [var loadingStrategy: AudioFileResource.LoadingStrategy](audiofileresource/loadingstrategy-swift.property.md)
  The resource’s memory model.
- [var shouldLoop: Bool](audiofileresource/shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/loadasync(named:in:inputmode:loadingstrategy:shouldloop:))*