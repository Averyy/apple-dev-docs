# loadBodyTrackedAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Asynchronously loads a body-tracked entity from a file URL.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0 (renamed: BodyTrackedEntity.init(contentsOf:withName:))
- iPadOS 13.0+ - Deprecated in 18.0 (renamed: BodyTrackedEntity.init(contentsOf:withName:))
- Mac Catalyst 13.0+ - Deprecated in 18.0 (renamed: BodyTrackedEntity.init(contentsOf:withName:))

## Declaration

```swift
@MainActor
@preconcurrency static func loadBodyTrackedAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<BodyTrackedEntity>
```

#### Return Value

A resource loader that publishes the root entity in the loaded file as a [`BodyTrackedEntity`](../bodytrackedentity.md).

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

### Loading a flattened body-tracked entity
- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](./loadbodytracked%28named,in%29.md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](./loadbodytracked%28contentsof,withname%29.md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(named: String, in: Bundle?) -> LoadRequest<BodyTrackedEntity>](./loadbodytrackedasync%28named,in%29.md)
  Asynchronously loads a body-tracked entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadbodytrackedasync(contentsof:withname:))*