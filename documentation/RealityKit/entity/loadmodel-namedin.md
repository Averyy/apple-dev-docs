# loadModel(named:in:)

**Framework**: RealityKit  
**Kind**: method

Synchronously loads a model entity from a bundle.

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
@preconcurrency static func loadModel(named name: String, in bundle: Bundle? = nil) throws -> ModelEntity
```

## Mentions

- [Loading entities from a file](loading-entities-from-a-file.md)
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)

#### Return Value

The root entity in the loaded file, which Reality Kit casts as a [`ModelEntity`](modelentity.md).

#### Discussion

Loading an [`Entity`](entity.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](entity/init(named:in:).md) for an example that demonstrates how to safely load content.

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func loadModel(contentsOf: URL, withName: String?) throws -> ModelEntity](entity/loadmodel(contentsof:withname:).md)
  Synchronously loads a model entity from a file URL.
- [static func loadModelAsync(named: String, in: Bundle?) -> LoadRequest<ModelEntity>](entity/loadmodelasync(named:in:).md)
  Asynchronously loads a model entity from a bundle.
- [static func loadModelAsync(contentsOf: URL, withName: String?) -> LoadRequest<ModelEntity>](entity/loadmodelasync(contentsof:withname:).md)
  Returns a load request that creates a model entity by asynchronously loading it from a file URL and flattening the model entity’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadmodel(named:in:))*