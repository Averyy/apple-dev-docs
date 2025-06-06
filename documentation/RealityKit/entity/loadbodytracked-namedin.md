# loadBodyTracked(named:in:)

**Framework**: RealityKit  
**Kind**: method

Synchronously loads a body-tracked entity from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadBodyTracked(named name: String, in bundle: Bundle? = nil) throws -> BodyTrackedEntity
```

## Mentions

- [Loading entities from a file](loading-entities-from-a-file.md)

#### Return Value

The root entity in the loaded file, cast as a [`BodyTrackedEntity`](bodytrackedentity.md).

#### Discussion

Loading an [`Entity`](entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](entity/init(named:in:).md) for an example that demonstrates how to safely load content.

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](entity/loadbodytracked(contentsof:withname:).md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(contentsOf: URL, withName: String?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(contentsof:withname:).md)
  Asynchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(named: String, in: Bundle?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(named:in:).md)
  Asynchronously loads a body-tracked entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadbodytracked(named:in:))*