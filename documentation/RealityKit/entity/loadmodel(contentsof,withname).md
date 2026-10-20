# loadModel(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Synchronously loads a model entity from a file URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadModel(contentsOf url: URL, withName resourceName: String? = nil) throws -> ModelEntity
```

#### Return Value

The root entity in the loaded file, which Reality Kit casts as a [`ModelEntity`](../modelentity.md).

#### Discussion

Loading an [`Entity`](../entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](./init%28named,in%29.md) for an example that demonstrates how to safely load content.

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

### Loading a flattened model entity
- [static func loadModel(named: String, in: Bundle?) throws -> ModelEntity](./loadmodel%28named,in%29.md)
  Synchronously loads a model entity from a bundle.
- [static func loadModelAsync(named: String, in: Bundle?) -> LoadRequest<ModelEntity>](./loadmodelasync%28named,in%29.md)
  Asynchronously loads a model entity from a bundle.
- [static func loadModelAsync(contentsOf: URL, withName: String?) -> LoadRequest<ModelEntity>](./loadmodelasync%28contentsof,withname%29.md)
  Returns a load request that creates a model entity by asynchronously loading it from a file URL and flattening the model entity’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadmodel(contentsof:withname:))*