# loadAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Returns a load request that creates an entity by asynchronously loading it from a file URL and preserving the entity’s hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<Entity>
```

#### Discussion

RealityKit supports loading entities from USD (`.usd`, `.usda`, `.usdc`, `.usdz`) and Reality (`.reality`) files. For Reality files that contain multiple scenes, specify which scene to load by appending a URL fragment with the scene name — for example, `my.reality#MyScene`.

For more information on loading entities, see [`Loading entities from a file`](loading-entities-from-a-file.md).

## Parameters

- `url`: A file URL representing the file to load. For Reality files, append a URL fragment to specify a scene name — for example, `my.reality#MyScene`.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

- [static func load(named: String, in: Bundle?) throws -> Entity](entity/load(named:in:).md)
  Returns an entity by synchronously loading it from a bundle.
- [static func load(contentsOf: URL, withName: String?) throws -> Entity](entity/load(contentsof:withname:).md)
  Returns an entity by synchronously loading it from a file URL.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<Entity>](entity/loadasync(named:in:).md)
  Returns a load request that creates an entity by asynchronously loading it from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadasync(contentsof:withname:))*