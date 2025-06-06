# loadModelAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Returns a load request that creates a model entity by asynchronously loading it from a file URL and flattening the model entity’s hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadModelAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<ModelEntity>
```

## Mentions

- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)

#### Discussion

For more information on loading entities, see [`Loading entities from a file`](loading-entities-from-a-file.md).

## Parameters

- `url`: The location of a file that represents an entity.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [static func loadModel(named: String, in: Bundle?) throws -> ModelEntity](entity/loadmodel(named:in:).md)
  Synchronously loads a model entity from a bundle.
- [static func loadModel(contentsOf: URL, withName: String?) throws -> ModelEntity](entity/loadmodel(contentsof:withname:).md)
  Synchronously loads a model entity from a file URL.
- [static func loadModelAsync(named: String, in: Bundle?) -> LoadRequest<ModelEntity>](entity/loadmodelasync(named:in:).md)
  Asynchronously loads a model entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadmodelasync(contentsof:withname:))*