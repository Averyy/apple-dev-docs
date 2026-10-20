# ComputeNodeGraph.NodeDefinition.Kind

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

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
enum Kind
```

## Topics

### Enumeration Cases
- [case binaryArithmetic(a: ComputeNodeGraph.DataType, b: ComputeNodeGraph.DataType, operation: BinaryOperation)](./kind-swift.enum/binaryarithmetic%28a,b,operation%29.md)
  An arithmetic node with two operands of the given type, performing the specified operation
- [ComputeNodeGraph.NodeDefinition.Kind.compose(type:)](./kind-swift.enum/compose%28type%29.md)
  A node which composes a structure or vector type from its components
- [case convert(from: ComputeNodeGraph.DataType, to: ComputeNodeGraph.DataType)](./kind-swift.enum/convert%28from,to%29.md)
  Convert from one primitive MTLDataType to another.
- [ComputeNodeGraph.NodeDefinition.Kind.decompose(type:)](./kind-swift.enum/decompose%28type%29.md)
  A node which decomposes a structure or vector type, providing access to individual components
- [ComputeNodeGraph.NodeDefinition.Kind.fieldReference(type:)](./kind-swift.enum/fieldreference%28type%29.md)
  Node contains a reference to a field of another stage, containing the given layout
- [ComputeNodeGraph.NodeDefinition.Kind.function(name:bundle:)](./kind-swift.enum/function%28name,bundle%29.md)
  Node refers to a MTLFunction with name and optional bundle.
- [ComputeNodeGraph.NodeDefinition.Kind.graphGlobal](./kind-swift.enum/graphglobal.md)
  A node which contains global constants affecting the graph
- [ComputeNodeGraph.NodeDefinition.Kind.graphInput](./kind-swift.enum/graphinput.md)
  Return a uniform value supplied externally.
- [case loadState(definition: ComputeNodeGraph.StateDefinition)](./kind-swift.enum/loadstate%28definition%29.md)
  Node loads stored state into the graph
- [case reinterpret(from: ComputeNodeGraph.DataType, to: ComputeNodeGraph.DataType)](./kind-swift.enum/reinterpret%28from,to%29.md)
  Reinterpret one type scalar or vector type as another of the same number of size and bytes.
- [case sampleTexture(sampler: ComputeNodeGraph.SamplerSettings)](./kind-swift.enum/sampletexture%28sampler%29.md)
  A texture sampling operation with specified settings.
- [ComputeNodeGraph.NodeDefinition.Kind.stage(type:)](./kind-swift.enum/stage%28type%29.md)
  Node represents an execution stage in the graph, for example ‘simulation’ or ‘emission’
- [case standardLibrary(type: ComputeNodeGraph.DataType, function: StandardLibraryFunction)](./kind-swift.enum/standardlibrary%28type,function%29.md)
  A call to a standard library function with the specified data type.
- [case storeState(definition: ComputeNodeGraph.StateDefinition)](./kind-swift.enum/storestate%28definition%29.md)
  Node stores state into the graph.
- [case swizzle(type: ComputeNodeGraph.DataType, channels: ComputeNodeGraph.SwizzleChannels)](./kind-swift.enum/swizzle%28type,channels%29.md)
  A swizzle operation for the given vector data type and channel specification
- [ComputeNodeGraph.NodeDefinition.Kind.textureReference(port:)](./kind-swift.enum/texturereference%28port%29.md)
- [case unaryArithmetic(type: ComputeNodeGraph.DataType, operation: UnaryOperation)](./kind-swift.enum/unaryarithmetic%28type,operation%29.md)
  An arithmetic node with one operand of the given data type, performing the specified operation

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition/kind-swift.enum)*