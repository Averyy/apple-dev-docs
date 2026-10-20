# ComputeNodeGraph.StructureDefinition

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

A named structure type, pairing a type name with its in-memory layout.

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
struct StructureDefinition
```

#### Overview

A structure definition describes a composite value that can flow through a compute graph. It associates a Swift- or Metal-visible type name with a [`ComputeNodeGraph.StructureLayout`](./structurelayout.md) that lays out the structure’s members, their offsets, and its overall size and stride.

Use a structure definition to refer to user-defined aggregate types from other graph types, such as [`ComputeNodeGraph.ValueType.structure(definition:)`](./valuetype/structure%28definition%29.md) or `ComputeNodeGraph/StateType/structure(typeName:layout:)`.

## Topics

### Initializers
- [init(typeName: String, layout: ComputeNodeGraph.StructureLayout)](./structuredefinition/init%28typename,layout%29.md)
### Instance Properties
- [var layout: ComputeNodeGraph.StructureLayout](./structuredefinition/layout.md)
  The in-memory layout of the structure’s members.
- [var typeName: String](./structuredefinition/typename.md)
  The name used to refer to the structure type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/structuredefinition)*