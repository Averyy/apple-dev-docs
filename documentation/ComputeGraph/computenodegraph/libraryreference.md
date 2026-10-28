# ComputeNodeGraph.LibraryReference

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

A Metal library and an optional bundle identifier that locates shader functions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct LibraryReference
```

## Overview

Use `addLibrary(_:bundle:)` rather than constructing this type directly.

## Topics

### Initializers
- [init(library: any MTLLibrary, bundle: String?)](./libraryreference/init%28library,bundle%29.md)
### Instance Properties
- [var bundle: String?](./libraryreference/bundle.md)
  The bundle identifier used to scope shader function lookup, or `nil` if the library does not require one.
- [var library: any MTLLibrary](./libraryreference/library.md)
  The Metal library containing compiled shader functions.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Graph definition and assembly
- [struct ComputeNodeGraph](../computenodegraph.md)
- [ComputeNodeGraph.Assembly](./assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.Pipelines](./pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](./pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.NodeDefinition](./nodedefinition.md)
- [ComputeNodeGraph.Library](./library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/libraryreference)*