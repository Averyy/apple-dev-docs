# loadModelAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads a model entity from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadModelAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<ModelEntity>
```

## Mentions

- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)

#### Return Value

A resource loader that publishes the root entity in the loaded file as a [`ModelEntity`](modelentity.md).

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func loadModel(named: String, in: Bundle?) throws -> ModelEntity](entity/loadmodel(named:in:).md)
  Synchronously loads a model entity from a bundle.
- [static func loadModel(contentsOf: URL, withName: String?) throws -> ModelEntity](entity/loadmodel(contentsof:withname:).md)
  Synchronously loads a model entity from a file URL.
- [static func loadModelAsync(contentsOf: URL, withName: String?) -> LoadRequest<ModelEntity>](entity/loadmodelasync(contentsof:withname:).md)
  Returns a load request that creates a model entity by asynchronously loading it from a file URL and flattening the model entity’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadmodelasync(named:in:))*