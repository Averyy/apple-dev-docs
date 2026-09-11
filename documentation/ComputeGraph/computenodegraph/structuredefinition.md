# ComputeNodeGraph.StructureDefinition

**Framework**: Compute Graph  
**Kind**: struct

A named structure type, pairing a type name with its in-memory layout.

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
struct StructureDefinition
```

#### Overview

A structure definition describes a composite value that can flow through a compute graph. It associates a Swift- or Metal-visible type name with a [`ComputeNodeGraph.StructureLayout`](computenodegraph/structurelayout.md) that lays out the structure’s members, their offsets, and its overall size and stride.

Use a structure definition to refer to user-defined aggregate types from other graph types, such as [`ComputeNodeGraph.ValueType.structure(definition:)`](computenodegraph/valuetype/structure(definition:).md) or `ComputeNodeGraph/StateType/structure(typeName:layout:)`.

## Topics

### Initializers
- [init(typeName: String, layout: ComputeNodeGraph.StructureLayout)](computenodegraph/structuredefinition/init(typename:layout:).md)
### Instance Properties
- [var layout: ComputeNodeGraph.StructureLayout](computenodegraph/structuredefinition/layout.md)
  The in-memory layout of the structure’s members.
- [var typeName: String](computenodegraph/structuredefinition/typename.md)
  The name used to refer to the structure type.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/structuredefinition)*