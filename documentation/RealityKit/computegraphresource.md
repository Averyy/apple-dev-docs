# ComputeGraphResource

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A loaded compute graph resource containing the graph definition, compiled pipelines, and all associated rendering assets.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class ComputeGraphResource
```

## Overview

Load a `ComputeGraphResource` from a file URL using [`init(contentsOf:bundle:)`](./computegraphresource/init%28contentsof,bundle%29.md), then assign it to a [`resource`](./computegraphcomponent/resource.md) to drive a simulation.

```swift
let resource = try await ComputeGraphResource(contentsOf: url)
var component = ComputeGraphComponent(resource: resource)
entity.components.set(component)
```

## Topics

### Structures
- [ComputeGraphResource.BufferInfo](./computegraphresource/bufferinfo.md)
- [ComputeGraphResource.Dependencies](./computegraphresource/dependencies.md)
### Initializers
- [convenience init(contentsOf: URL) async throws](./computegraphresource/init%28contentsof%29.md)
- [convenience init(contentsOf: URL, bundle: Bundle?) async throws](./computegraphresource/init%28contentsof,bundle%29.md)
- [convenience init(graph: ComputeNodeGraph, pipelines: ComputeNodeGraph.Pipelines, dependencies: ComputeGraphResource.Dependencies) throws](./computegraphresource/init%28graph,pipelines,dependencies%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphresource)*