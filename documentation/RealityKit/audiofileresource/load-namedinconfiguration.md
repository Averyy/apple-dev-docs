# load(named:in:configuration:)

**Framework**: RealityKit  
**Kind**: method

Loads an AudioFileResource synchronously.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func load(named name: String, in bundle: Bundle? = nil, configuration: AudioFileResource.Configuration = .init()) throws -> AudioFileResource
```

#### Discussion

> ❗ **Important**: The name provided  be unique.

The name provided  be unique.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/load(named:in:configuration:))*