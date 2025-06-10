# loadAnchor(named:in:)

**Framework**: RealityKit  
**Kind**: method

Synchronously loads an anchor entity from a bundle.

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
@preconcurrency static func loadAnchor(named name: String, in bundle: Bundle? = nil) throws -> AnchorEntity
```

## Mentions

- [Loading entities from a file](loading-entities-from-a-file.md)

#### Return Value

The root entity in the loaded file, which Reality Kit casts as an [`AnchorEntity`](anchorentity.md).

#### Discussion

Loading an [`Entity`](entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](entity/init(named:in:).md) for an example that demonstrates how to safely load content.

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func loadAnchor(contentsOf: URL, withName: String?) throws -> AnchorEntity](entity/loadanchor(contentsof:withname:).md)
  Synchronously loads an anchor entity from a file URL.
- [static func loadAnchorAsync(named: String, in: Bundle?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(named:in:).md)
  Asynchronously loads an anchor entity from a bundle.
- [static func loadAnchorAsync(contentsOf: URL, withName: String?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(contentsof:withname:).md)
  Asynchronously loads an anchor entity from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadanchor(named:in:))*