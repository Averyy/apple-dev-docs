# loadingStrategy

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The resource’s memory model.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- visionOS 2.0+ - Deprecated in 1.0

> **Deprecated**: Use configuration.loadingStrategy instead.

## Declaration

```swift
@MainActor
@preconcurrency var loadingStrategy: AudioFileResource.LoadingStrategy { get set }
```

## See Also

### Deprecated
- [static func load(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](./load%28named,in,inputmode,loadingstrategy,shouldloop%29.md)
  Synchronously loads an audio resource.
- [static func loadAsync(named: String, in: Bundle?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](./loadasync%28named,in,inputmode,loadingstrategy,shouldloop%29.md)
- [static func load(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) throws -> AudioFileResource](./load%28contentsof,withname,inputmode,loadingstrategy,shouldloop%29.md)
  Synchronously loads an audio resource.
- [static func loadAsync(contentsOf: URL, withName: String?, inputMode: AudioResource.InputMode, loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool) -> LoadRequest<AudioFileResource>](./loadasync%28contentsof,withname,inputmode,loadingstrategy,shouldloop%29.md)
- [var shouldLoop: Bool](./shouldloop.md)
  Whether or not this file loops during playback. This should be set for assets that are prepared as seamless loops. A looping resource will play forever until it is explicitly told to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/loadingstrategy-swift.property)*