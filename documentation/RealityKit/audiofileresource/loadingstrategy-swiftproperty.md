# loadingStrategy

**Framework**: RealityKit  
**Kind**: property

The resource’s memory model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var loadingStrategy: AudioFileResource.LoadingStrategy { get set }
```

## See Also

- [static func load(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](audiofileresource/load(named:in:inputmode:loadingstrategy:shouldloop:).md)
  Synchronously loads an audio resource.
- [static func loadAsync(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](audiofileresource/loadasync(named:in:inputmode:loadingstrategy:shouldloop:).md)
- [static func load(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](audiofileresource/load(contentsof:withname:inputmode:loadingstrategy:shouldloop:).md)
  Synchronously loads an audio resource.
- [static func loadAsync(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](audiofileresource/loadasync(contentsof:withname:inputmode:loadingstrategy:shouldloop:).md)
- [var shouldLoop: Bool](audiofileresource/shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/loadingstrategy-swift.property)*