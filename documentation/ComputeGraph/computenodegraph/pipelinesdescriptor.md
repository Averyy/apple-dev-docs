# ComputeNodeGraph.PipelinesDescriptor

**Framework**: ComputeGraph  
**Kind**: struct

Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
struct PipelinesDescriptor
```

#### Overview

Use a descriptor when you need explicit control over pipeline compilation — for example, to supply Metal libraries from multiple bundles or to enable debug draw. Pass the configured descriptor to `ComputeNodeGraph.Pipelines/init(descriptor:)` to compile.

```swift
var descriptor = ComputeNodeGraph.PipelinesDescriptor(assembly: assembly)
descriptor.addLibrary(myMTLLibrary, bundle: "com.example.MyEffects")
descriptor.options.debugDraw = true
let pipelines = try await ComputeNodeGraph.Pipelines(descriptor: descriptor)
```

## Topics

### Initializers
- [init(assembly: ComputeNodeGraph.Assembly)](computenodegraph/pipelinesdescriptor/init(assembly:).md)
  Creates a descriptor configured for the given graph assembly.
### Instance Properties
- [var assembly: ComputeNodeGraph.Assembly](computenodegraph/pipelinesdescriptor/assembly.md)
  The assembled compute graph layout that defines the graph’s buffer, uniform, and texture configuration.
- [var libraries: [ComputeNodeGraph.LibraryReference]](computenodegraph/pipelinesdescriptor/libraries.md)
  The Metal libraries that provide shader function implementations for the graph’s nodes.
- [var options: ComputeNodeGraph.Pipelines.Options](computenodegraph/pipelinesdescriptor/options.md)
  Options controlling pipeline compilation, such as whether debug draw is enabled.
### Instance Methods
- [func addLibrary(any MTLLibrary, bundle: String?)](computenodegraph/pipelinesdescriptor/addlibrary(_:bundle:).md)
- [func setLibrary(ComputeNodeGraph.Library)](computenodegraph/pipelinesdescriptor/setlibrary(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/pipelinesdescriptor)*