# loadAsync(named:in:inputMode:loadingStrategy:shouldLoop:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 13.0+ - Deprecated in 18.0 (renamed: AudioFileResource.init(named:in:configuration:))
- iPadOS 13.0+ - Deprecated in 18.0 (renamed: AudioFileResource.init(named:in:configuration:))
- Mac Catalyst 13.0+ - Deprecated in 18.0 (renamed: AudioFileResource.init(named:in:configuration:))
- macOS 10.15+ - Deprecated in 15.0 (renamed: AudioFileResource.init(named:in:configuration:))

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(named name: String, in bundle: Bundle? = nil, inputMode: AudioResource.InputMode = .spatial, loadingStrategy: AudioFileResource.LoadingStrategy = .preload, shouldLoop: Bool = false) -> LoadRequest<AudioFileResource>
```

## See Also

### Deprecated
- [static func load(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](./load%28named,in,inputmode,loadingstrategy,shouldloop%29.md)
  Synchronously loads an audio resource.
- [static func load(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](./load%28contentsof,withname,inputmode,loadingstrategy,shouldloop%29.md)
  Synchronously loads an audio resource.
- [static func loadAsync(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](./loadasync%28contentsof,withname,inputmode,loadingstrategy,shouldloop%29.md)
- [var loadingStrategy: AudioFileResource.LoadingStrategy](./loadingstrategy-swift.property.md)
  The resource’s memory model.
- [var shouldLoop: Bool](./shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/loadasync(named:in:inputmode:loadingstrategy:shouldloop:))*