# ComputeNodeGraph.StateType

**Framework**: Compute Graph  
**Kind**: enum

The shape of a value stored in a compute graph’s state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
enum StateType
```

#### Overview

`StateType` describes what kind of value a state holds. The shape determines the slot’s size, alignment, and how it is surfaced in generated Metal source and in graph serialization.

## Topics

### Enumeration Cases
- [case array(definition: ComputeNodeGraph.ArrayDefinition)](computenodegraph/statetype/array(definition:).md)
  Value is an array with the provided definition
- [ComputeNodeGraph.StateType.data(length:)](computenodegraph/statetype/data(length:).md)
  Value is a fixed number of untyped bytes
- [ComputeNodeGraph.StateType.dataType(type:)](computenodegraph/statetype/datatype(type:).md)
  Legacy. Do not construct in new code.
- [case primitive(type: ComputeNodeGraph.DataType)](computenodegraph/statetype/primitive(type:).md)
  Value is a primitive with the given type
- [case structure(definition: ComputeNodeGraph.StructureDefinition)](computenodegraph/statetype/structure(definition:).md)
  Value is a structure with the given layout
### Instance Methods
- [func loadBuffer(from: Data) throws -> (data: Data, elementCount: Int)](computenodegraph/statetype/loadbuffer(from:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/statetype)*