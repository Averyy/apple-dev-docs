# loadBodyTrackedAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads a body-tracked entity from a file URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadBodyTrackedAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<BodyTrackedEntity>
```

#### Return Value

A resource loader that publishes the root entity in the loaded file as a [`BodyTrackedEntity`](bodytrackedentity.md).

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](entity/loadbodytracked(named:in:).md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](entity/loadbodytracked(contentsof:withname:).md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(named: String, in: Bundle?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(named:in:).md)
  Asynchronously loads a body-tracked entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadbodytrackedasync(contentsof:withname:))*