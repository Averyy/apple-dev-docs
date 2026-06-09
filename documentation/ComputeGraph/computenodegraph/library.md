# ComputeNodeGraph.Library

**Framework**: ComputeGraph  
**Kind**: class

A class defining a library of node definitions that can be added to a ComputeNodeGraph

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
final class Library
```

#### Overview

A Library contains definitions and also stores MTLFunction implementations for built-in nodes and you can construct new libraries containing nodes you provide.

These nodes are functions implemented using the Metal Shading Language and annotated with the `[[stitchable]]` attribute.

## Topics

### Initializers
- [init()](computenodegraph/library/init.md)
- [convenience init?(bundle: Bundle)](computenodegraph/library/init(bundle:).md)
  Creates a library from the Metal default library in the given bundle, if available.
- [convenience init(from: any MTLLibrary, bundleIdentifier: String?)](computenodegraph/library/init(from:bundleidentifier:).md)
  Creates a library by extracting node definitions from a Metal library.
### Instance Properties
- [var definitions: [ComputeNodeGraph.NodeDefinition]](computenodegraph/library/definitions.md)
  The collection of all node definitions available in this library.
### Instance Methods
- [func definition(named: String, in: String?) -> ComputeNodeGraph.NodeDefinition?](computenodegraph/library/definition(named:in:).md)
  Returns the first node definition with the given name, or `nil` if none is found.
- [func definition(stage: ComputeNodeGraph.Stage) -> ComputeNodeGraph.NodeDefinition?](computenodegraph/library/definition(stage:).md)
  Returns a definition for the given stage.
- [func definitionsMatching(input: ComputeNodeGraph.ValueType) -> [ComputeNodeGraph.NodeDefinition]](computenodegraph/library/definitionsmatching(input:).md)
  Returns all definitions that have at least one input matching the given value type.
- [func definitionsMatching(inputs: [ComputeNodeGraph.ValueType]) -> [ComputeNodeGraph.NodeDefinition]](computenodegraph/library/definitionsmatching(inputs:).md)
  Returns all definitions whose user-editable inputs, in order, match the given value types.
- [func definitionsMatching(output: ComputeNodeGraph.ValueType) -> [ComputeNodeGraph.NodeDefinition]](computenodegraph/library/definitionsmatching(output:).md)
  Returns all definitions that have at least one output matching the given value type.
- [func merge(contentsOf: ComputeNodeGraph.Library)](computenodegraph/library/merge(contentsof:).md)
  Merges nodes from specified library into this library.
### Type Properties
- [static let shared: ComputeNodeGraph.Library](computenodegraph/library/shared.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library)*