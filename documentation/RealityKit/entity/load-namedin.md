# load(named:in:)

**Framework**: RealityKit  
**Kind**: method

Returns an entity by synchronously loading it from a bundle.

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
@preconcurrency static func load(named name: String, in bundle: Bundle? = nil) throws -> Entity
```

## Mentions

- [Loading remote assets in multiplayer apps](loading-remote-assets.md)

#### Return Value

The root entity in the loaded file.

#### Discussion

Loading an [`Entity`](entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](entity/init(named:in:).md) for an example that demonstrates how to safely load content.

RealityKit supports loading entities from USD (`.usd`, `.usda`, `.usdc`, `.usdz`) and Reality (`.reality`) files.

When building your app, Xcode automatically converts any Reality Composer projects (`.rcproject`) in the selected target into Reality files, which it then copies into your app’s bundle.

For more information on loading entities, see [`Loading entities from a file`](loading-entities-from-a-file.md).

## Parameters

- `name`: The base name of the file to load.  An extension isn’t required,   but you can provide one to resolve collisions.  In the presence of a collision,   the provided name resolves with the following order of precedence:   [ ,  ,  ,  ].
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func load(contentsOf: URL, withName: String?) throws -> Entity](entity/load(contentsof:withname:).md)
  Returns an entity by synchronously loading it from a file URL.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<Entity>](entity/loadasync(named:in:).md)
  Returns a load request that creates an entity by asynchronously loading it from a bundle.
- [static func loadAsync(contentsOf: URL, withName: String?) -> LoadRequest<Entity>](entity/loadasync(contentsof:withname:).md)
  Returns a load request that creates an entity by asynchronously loading it from a file URL and preserving the entity’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/load(named:in:))*