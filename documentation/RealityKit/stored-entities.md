# Stored entities

**Framework**: RealityKit

Manage entities that you store as assets on disk.

#### Overview

If you bundle 3D assets with your app, or download them from the network into local file storage, you need a way to load them at runtime. RealityKit provides a collection of methods that you use to load USD and Reality files into [`Entity`](entity.md) instances.

## Topics

### Essentials
- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [class LoadRequest](loadrequest.md)
  A resource loader that acts as a publisher.
### Loading an entity hierarchy
- [static func load(named: String, in: Bundle?) throws -> Entity](entity/load(named:in:).md)
  Returns an entity by synchronously loading it from a bundle.
- [static func load(contentsOf: URL, withName: String?) throws -> Entity](entity/load(contentsof:withname:).md)
  Returns an entity by synchronously loading it from a file URL.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<Entity>](entity/loadasync(named:in:).md)
  Returns a load request that creates an entity by asynchronously loading it from a bundle.
- [static func loadAsync(contentsOf: URL, withName: String?) -> LoadRequest<Entity>](entity/loadasync(contentsof:withname:).md)
  Returns a load request that creates an entity by asynchronously loading it from a file URL and preserving the entity’s hierarchy.
### Loading an anchor entity
- [static func loadAnchor(named: String, in: Bundle?) throws -> AnchorEntity](entity/loadanchor(named:in:).md)
  Synchronously loads an anchor entity from a bundle.
- [static func loadAnchor(contentsOf: URL, withName: String?) throws -> AnchorEntity](entity/loadanchor(contentsof:withname:).md)
  Synchronously loads an anchor entity from a file URL.
- [static func loadAnchorAsync(named: String, in: Bundle?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(named:in:).md)
  Asynchronously loads an anchor entity from a bundle.
- [static func loadAnchorAsync(contentsOf: URL, withName: String?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(contentsof:withname:).md)
  Asynchronously loads an anchor entity from a file URL.
### Loading a flattened model entity
- [static func loadModel(named: String, in: Bundle?) throws -> ModelEntity](entity/loadmodel(named:in:).md)
  Synchronously loads a model entity from a bundle.
- [static func loadModel(contentsOf: URL, withName: String?) throws -> ModelEntity](entity/loadmodel(contentsof:withname:).md)
  Synchronously loads a model entity from a file URL.
- [static func loadModelAsync(named: String, in: Bundle?) -> LoadRequest<ModelEntity>](entity/loadmodelasync(named:in:).md)
  Asynchronously loads a model entity from a bundle.
- [static func loadModelAsync(contentsOf: URL, withName: String?) -> LoadRequest<ModelEntity>](entity/loadmodelasync(contentsof:withname:).md)
  Returns a load request that creates a model entity by asynchronously loading it from a file URL and flattening the model entity’s hierarchy.
### Loading a flattened body-tracked entity
- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](entity/loadbodytracked(named:in:).md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](entity/loadbodytracked(contentsof:withname:).md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(contentsOf: URL, withName: String?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(contentsof:withname:).md)
  Asynchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(named: String, in: Bundle?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(named:in:).md)
  Asynchronously loads a body-tracked entity from a bundle.

## See Also

- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [convenience init(contentsOf: URL, withName: String?) async throws](entity/init(contentsof:withname:).md)
  Creates an entity by asynchronously loading it from a file URL.
- [convenience init(named: String, in: Bundle?) async throws](entity/init(named:in:).md)
  Creates an entity by asynchronously loading it from a bundle.
- [struct ReferenceComponent](referencecomponent.md)
  A component that can load another entity from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/stored-entities)*