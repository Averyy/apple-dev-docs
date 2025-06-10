# init(named:in:configuration:)

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
@preconcurrency convenience init(named name: String, in bundle: Bundle? = nil, configuration: AudioFileResource.Configuration = .init()) async throws
```

#### Discussion

> ❗ **Important**: The name provided  be unique.

## See Also

- [convenience(named:from:in:)](audiofileresource/init(named:from:in:).md)
  Initializes a preconfigured AudioFileResource asynchronously from a Reality Composer Pro project with the given `name` as the the prim-path of the AudioFile, and the `scene` as the name of the USD file name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/init(named:in:configuration:))*