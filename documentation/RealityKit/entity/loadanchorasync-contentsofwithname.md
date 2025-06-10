# loadAnchorAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads an anchor entity from a file URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAnchorAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<AnchorEntity>
```

## Mentions

- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)
- [Taking Control of Scene Anchoring](taking-control-of-scene-anchoring.md)

#### Return Value

A resource loader that publishes the root entity in the loaded file as an [`AnchorEntity`](anchorentity.md).

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [static func loadAnchor(named: String, in: Bundle?) throws -> AnchorEntity](entity/loadanchor(named:in:).md)
  Synchronously loads an anchor entity from a bundle.
- [static func loadAnchor(contentsOf: URL, withName: String?) throws -> AnchorEntity](entity/loadanchor(contentsof:withname:).md)
  Synchronously loads an anchor entity from a file URL.
- [static func loadAnchorAsync(named: String, in: Bundle?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(named:in:).md)
  Asynchronously loads an anchor entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadanchorasync(contentsof:withname:))*