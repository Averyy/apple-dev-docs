# init(contentsOf:withName:configuration:)

**Framework**: RealityKit  
**Kind**: init

Initializes an AudioFileResource asynchronously.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(contentsOf url: URL, withName resourceName: String? = nil, configuration: AudioFileResource.Configuration = .init()) async throws
```

#### Discussion

> ❗ **Important**: The name provided  be unique.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/init(contentsof:withname:configuration:))*