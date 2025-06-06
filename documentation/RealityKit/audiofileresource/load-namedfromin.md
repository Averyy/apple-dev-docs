# load(named:from:in:)

**Framework**: RealityKit  
**Kind**: method

Loads a preconfigured AudioFileResource from a Reality Composer Pro project with the given `name` as the the prim-path of the AudioFile, and the `scene` as the name of the USD file name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func load(named name: String, from scene: String, in bundle: Bundle? = nil) throws -> AudioFileResource
```

#### Discussion

> ❗ **Important**: The name provided  be unique.

The name provided  be unique.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/load(named:from:in:))*