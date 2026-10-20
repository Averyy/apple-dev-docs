# loadBodyTrackedAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Asynchronously loads a body-tracked entity from a bundle.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0 (renamed: BodyTrackedEntity.init(named:in:))
- iPadOS 13.0+ - Deprecated in 18.0 (renamed: BodyTrackedEntity.init(named:in:))
- Mac Catalyst 13.0+ - Deprecated in 18.0 (renamed: BodyTrackedEntity.init(named:in:))

## Declaration

```swift
@MainActor
@preconcurrency static func loadBodyTrackedAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<BodyTrackedEntity>
```

#### Return Value

A resource loader that publishes the root entity in the loaded file as a [`BodyTrackedEntity`](../bodytrackedentity.md).

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use `nil` to search the app’s main bundle.

## See Also

### Loading a flattened body-tracked entity
- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](./loadbodytracked%28named,in%29.md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](./loadbodytracked%28contentsof,withname%29.md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(contentsOf: URL, withName: String?) -> LoadRequest<BodyTrackedEntity>](./loadbodytrackedasync%28contentsof,withname%29.md)
  Asynchronously loads a body-tracked entity from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadbodytrackedasync(named:in:))*