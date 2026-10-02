# ComputeNodeGraph.LibraryReference

**Framework**: Compute Graph  
**Kind**: struct

A Metal library and an optional bundle identifier that locates shader functions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
struct LibraryReference
```

#### Overview

Use `addLibrary(_:bundle:)` rather than constructing this type directly.

## Topics

### Initializers
- [init(library: any MTLLibrary, bundle: String?)](computenodegraph/libraryreference/init(library:bundle:).md)
### Instance Properties
- [var bundle: String?](computenodegraph/libraryreference/bundle.md)
  The bundle identifier used to scope shader function lookup, or `nil` if the library does not require one.
- [var library: any MTLLibrary](computenodegraph/libraryreference/library.md)
  The Metal library containing compiled shader functions.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ComputeNodeGraph](computenodegraph.md)
- [ComputeNodeGraph.Assembly](computenodegraph/assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.Pipelines](computenodegraph/pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](computenodegraph/pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.NodeDefinition](computenodegraph/nodedefinition.md)
- [ComputeNodeGraph.Library](computenodegraph/library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/libraryreference)*