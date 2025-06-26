# loadAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method

Returns a load request that creates an entity by asynchronously loading it from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<Entity>
```

## Mentions

- [Loading remote assets in multiplayer apps](loading-remote-assets.md)

#### Return Value

A resource loader that publishes the root entity in the loaded file.

#### Discussion

RealityKit supports loading entities from USD (`.usd`, `.usda`, `.usdc`, `.usdz`) and Reality (`.reality`) files.

When building your app, Xcode automatically converts any Reality Composer projects (`.rcproject`) in the selected target into Reality files, which it then copies into your app’s bundle.

For more information on loading entities, see [`Loading entities from a file`](loading-entities-from-a-file.md).

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func load(named: String, in: Bundle?) throws -> Entity](entity/load(named:in:).md)
  Returns an entity by synchronously loading it from a bundle.
- [static func load(contentsOf: URL, withName: String?) throws -> Entity](entity/load(contentsof:withname:).md)
  Returns an entity by synchronously loading it from a file URL.
- [static func loadAsync(contentsOf: URL, withName: String?) -> LoadRequest<Entity>](entity/loadasync(contentsof:withname:).md)
  Returns a load request that creates an entity by asynchronously loading it from a file URL and preserving the entity’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadasync(named:in:))*