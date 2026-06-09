# ComputeNodeGraph.NodeDefinition.Kind

**Framework**: ComputeGraph  
**Kind**: enum

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
enum Kind
```

## Topics

### Enumeration Cases
- [case binaryArithmetic(a: MTLDataType, b: MTLDataType, operation: BinaryOperation)](computenodegraph/nodedefinition/kind-swift.enum/binaryarithmetic(a:b:operation:).md)
  An arithmetic node with two operands of the given type, performing the specified operation
- [ComputeNodeGraph.NodeDefinition.Kind.compose(type:)](computenodegraph/nodedefinition/kind-swift.enum/compose(type:).md)
  A node which composes a structure or vector type from its components
- [ComputeNodeGraph.NodeDefinition.Kind.convert(from:to:)](computenodegraph/nodedefinition/kind-swift.enum/convert(from:to:).md)
  Convert from one primitive MTLDataType to another.
- [ComputeNodeGraph.NodeDefinition.Kind.decompose(type:)](computenodegraph/nodedefinition/kind-swift.enum/decompose(type:).md)
  A node which decomposes a structure or vector type, providing access to individual components
- [ComputeNodeGraph.NodeDefinition.Kind.fieldReference(type:)](computenodegraph/nodedefinition/kind-swift.enum/fieldreference(type:).md)
  Node contains a reference to a field of another stage, containing the given layout
- [ComputeNodeGraph.NodeDefinition.Kind.function](computenodegraph/nodedefinition/kind-swift.enum/function.md)
  Node refers to a MTLFunction
- [ComputeNodeGraph.NodeDefinition.Kind.graphGlobal](computenodegraph/nodedefinition/kind-swift.enum/graphglobal.md)
  A node which contains global constants affecting the graph
- [ComputeNodeGraph.NodeDefinition.Kind.graphInput](computenodegraph/nodedefinition/kind-swift.enum/graphinput.md)
  Return a uniform value supplied externally.
- [case loadState(definition: ComputeNodeGraph.StateDefinition)](computenodegraph/nodedefinition/kind-swift.enum/loadstate(definition:).md)
  Node loads stored state into the graph
- [ComputeNodeGraph.NodeDefinition.Kind.reinterpret(from:to:)](computenodegraph/nodedefinition/kind-swift.enum/reinterpret(from:to:).md)
  Reinterpret one type scalar or vector type as another of the same number of size and bytes.
- [ComputeNodeGraph.NodeDefinition.Kind.sampleTexture(_:)](computenodegraph/nodedefinition/kind-swift.enum/sampletexture(_:).md)
  A texture sampling operation with specified settings.
- [ComputeNodeGraph.NodeDefinition.Kind.stage(type:)](computenodegraph/nodedefinition/kind-swift.enum/stage(type:).md)
  Node represents an execution stage in the graph, for example ‘simulation’ or ‘emission’
- [case standardLibrary(type: MTLDataType, function: StandardLibraryFunction)](computenodegraph/nodedefinition/kind-swift.enum/standardlibrary(type:function:).md)
  A call to a standard library function with the specified data type.
- [case storeState(definition: ComputeNodeGraph.StateDefinition)](computenodegraph/nodedefinition/kind-swift.enum/storestate(definition:).md)
  Node stores state into the graph.
- [case swizzle(type: MTLDataType, channels: ComputeNodeGraph.SwizzleChannels)](computenodegraph/nodedefinition/kind-swift.enum/swizzle(type:channels:).md)
  A swizzle operation for the given vector data type and channel specification
- [ComputeNodeGraph.NodeDefinition.Kind.textureReference(port:)](computenodegraph/nodedefinition/kind-swift.enum/texturereference(port:).md)
- [ComputeNodeGraph.NodeDefinition.Kind.unaryArithmetic(type:operation:)](computenodegraph/nodedefinition/kind-swift.enum/unaryarithmetic(type:operation:).md)
  An arithmetic node with one operand of the given data type, performing the specified operation

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition/kind-swift.enum)*