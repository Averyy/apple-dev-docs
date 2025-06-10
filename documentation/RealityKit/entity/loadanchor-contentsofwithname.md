# loadAnchor(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Synchronously loads an anchor entity from a file URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAnchor(contentsOf url: URL, withName resourceName: String? = nil) throws -> AnchorEntity
```

## Mentions

- [Taking Control of Scene Anchoring](taking-control-of-scene-anchoring.md)
- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)

#### Return Value

The root entity in the loaded file, which Reality Kit casts as an [`AnchorEntity`](anchorentity.md).

#### Discussion

Loading an [`Entity`](entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](entity/init(named:in:).md) for an example that demonstrates how to safely load content.

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [static func loadAnchor(named: String, in: Bundle?) throws -> AnchorEntity](entity/loadanchor(named:in:).md)
  Synchronously loads an anchor entity from a bundle.
- [static func loadAnchorAsync(named: String, in: Bundle?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(named:in:).md)
  Asynchronously loads an anchor entity from a bundle.
- [static func loadAnchorAsync(contentsOf: URL, withName: String?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(contentsof:withname:).md)
  Asynchronously loads an anchor entity from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadanchor(contentsof:withname:))*