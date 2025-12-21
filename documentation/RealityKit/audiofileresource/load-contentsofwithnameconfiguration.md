# load(contentsOf:withName:configuration:)

**Framework**: RealityKit  
**Kind**: method

Loads an AudioFileResource synchronously.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func load(contentsOf url: URL, withName name: String? = nil, configuration: AudioFileResource.Configuration = .init()) throws -> AudioFileResource
```

#### Discussion

> ❗ **Important**: The name provided  be unique.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/load(contentsof:withname:configuration:))*