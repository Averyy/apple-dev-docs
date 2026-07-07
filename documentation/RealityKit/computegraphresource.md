# ComputeGraphResource

**Framework**: RealityKit  
**Kind**: class

A loaded compute graph resource containing the graph definition, compiled pipelines, and all associated rendering assets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ComputeGraphResource
```

#### Overview

Load a `ComputeGraphResource` from a file URL using [`init(contentsOf:bundle:)`](computegraphresource/init(contentsof:bundle:).md), then assign it to a [`resource`](computegraphcomponent/resource.md) to drive a simulation.

```swift
let resource = try await ComputeGraphResource(contentsOf: url)
var component = ComputeGraphComponent(resource: resource)
entity.components.set(component)
```

## Topics

### Structures
- [ComputeGraphResource.BufferInfo](computegraphresource/bufferinfo.md)
- [ComputeGraphResource.Dependencies](computegraphresource/dependencies.md)
### Initializers
- [convenience init(contentsOf: URL) async throws](computegraphresource/init(contentsof:).md)
- [convenience init(contentsOf: URL, bundle: Bundle?) async throws](computegraphresource/init(contentsof:bundle:).md)
- [convenience init(graph: ComputeNodeGraph, pipelines: ComputeNodeGraph.Pipelines, dependencies: ComputeGraphResource.Dependencies) throws](computegraphresource/init(graph:pipelines:dependencies:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphresource)*