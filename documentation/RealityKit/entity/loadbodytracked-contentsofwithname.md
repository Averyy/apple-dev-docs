# loadBodyTracked(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Synchronously loads a body-tracked entity from a file URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadBodyTracked(contentsOf url: URL, withName resourceName: String? = nil) throws -> BodyTrackedEntity
```

#### Return Value

The root entity in the loaded file, cast as a [`BodyTrackedEntity`](bodytrackedentity.md).

#### Discussion

Loading an [`Entity`](entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](entity/init(named:in:).md) for an example that demonstrates how to safely load content.

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](entity/loadbodytracked(named:in:).md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTrackedAsync(contentsOf: URL, withName: String?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(contentsof:withname:).md)
  Asynchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(named: String, in: Bundle?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(named:in:).md)
  Asynchronously loads a body-tracked entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadbodytracked(contentsof:withname:))*