# ComputeNodeGraph.StateType

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

The shape of a value stored in a compute graph’s state.

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
enum StateType
```

## Overview

`StateType` describes what kind of value a state holds. The shape determines the slot’s size, alignment, and how it is surfaced in generated Metal source and in graph serialization.

## Topics

### Enumeration Cases
- [case array(definition: ComputeNodeGraph.ArrayDefinition)](./statetype/array%28definition%29.md)
  Value is an array with the provided definition
- [ComputeNodeGraph.StateType.data(length:)](./statetype/data%28length%29.md)
  Value is a fixed number of untyped bytes
- [ComputeNodeGraph.StateType.dataType(type:)](./statetype/datatype%28type%29.md)
  Legacy. Do not construct in new code.
- [case primitive(type: ComputeNodeGraph.DataType)](./statetype/primitive%28type%29.md)
  Value is a primitive with the given type
- [case structure(definition: ComputeNodeGraph.StructureDefinition)](./statetype/structure%28definition%29.md)
  Value is a structure with the given layout
### Instance Methods
- [func loadBuffer(from: Data) throws -> (data: Data, elementCount: Int)](./statetype/loadbuffer%28from%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/statetype)*