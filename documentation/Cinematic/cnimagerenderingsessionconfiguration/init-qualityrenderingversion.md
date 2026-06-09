# init(quality:renderingVersion:)

**Framework**: Cinematic  
**Kind**: init

Initialize with a specific rendering version.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
init?(quality: CNRenderingQuality, renderingVersion: Int)
```

## Parameters

- `quality`: The quality level for the rendering session.
- `renderingVersion`: Should be obtained from `latestRenderingVersion`. Pinning a version from a prior build ensures rendering output is stable across OS updates. Use `isRenderingVersionSupported:` to verify the version is still supported before using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsessionconfiguration/init(quality:renderingversion:))*