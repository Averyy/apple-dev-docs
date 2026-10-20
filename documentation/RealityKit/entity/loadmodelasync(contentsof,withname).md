# loadModelAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Returns a load request that creates a model entity by asynchronously loading it from a file URL and flattening the model entity’s hierarchy.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0 (renamed: ModelEntity.init(contentsOf:withName:))
- iPadOS 13.0+ - Deprecated in 18.0 (renamed: ModelEntity.init(contentsOf:withName:))
- Mac Catalyst 13.0+ - Deprecated in 18.0 (renamed: ModelEntity.init(contentsOf:withName:))
- macOS 10.15+ - Deprecated in 15.0 (renamed: ModelEntity.init(contentsOf:withName:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: ModelEntity.init(contentsOf:withName:))

## Declaration

```swift
@MainActor
@preconcurrency static func loadModelAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<ModelEntity>
```

#### Discussion

For more information on loading entities, see [Loading entities from a file](../loading-entities-from-a-file.md).

## Parameters

- `url`: The location of a file that represents an entity.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

### Loading a flattened model entity
- [static func loadModel(named: String, in: Bundle?) throws -> ModelEntity](./loadmodel%28named,in%29.md)
  Synchronously loads a model entity from a bundle.
- [static func loadModel(contentsOf: URL, withName: String?) throws -> ModelEntity](./loadmodel%28contentsof,withname%29.md)
  Synchronously loads a model entity from a file URL.
- [static func loadModelAsync(named: String, in: Bundle?) -> LoadRequest<ModelEntity>](./loadmodelasync%28named,in%29.md)
  Asynchronously loads a model entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadmodelasync(contentsof:withname:))*