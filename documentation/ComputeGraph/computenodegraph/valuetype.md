# ComputeNodeGraph.ValueType

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

Describes the storage and layout of a port’s value, ranging from Metal primitives and structures to opaque references and stateful bindings.

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
enum ValueType
```

## Topics

### Enumeration Cases
- [ComputeNodeGraph.ValueType.data(length:)](./valuetype/data%28length%29.md)
  Value contains fixed-length data of the given length.
- [ComputeNodeGraph.ValueType.dataType(type:)](./valuetype/datatype%28type%29.md)
  Legacy. Do not construct in new code.
- [ComputeNodeGraph.ValueType.enumeration(typeName:)](./valuetype/enumeration%28typename%29.md)
  Value is from enumeration with the given typeName
- [ComputeNodeGraph.ValueType.none](./valuetype/none.md)
  No storage for this value.
- [ComputeNodeGraph.ValueType.opaque(typeName:)](./valuetype/opaque%28typename%29.md)
  Value is an opaque value of the given type
- [case pointer(type: ComputeNodeGraph.PointerDefinition)](./valuetype/pointer%28type%29.md)
- [case primitive(type: ComputeNodeGraph.DataType)](./valuetype/primitive%28type%29.md)
  Value is stored as a primitive data type.
- [case state(definition: ComputeNodeGraph.StateDefinition)](./valuetype/state%28definition%29.md)
  Value is a stored state value
- [ComputeNodeGraph.ValueType.string](./valuetype/string.md)
  Value is a utf-8 encoded string
- [case structure(definition: ComputeNodeGraph.StructureDefinition)](./valuetype/structure%28definition%29.md)
  Value is a structure with the given definition.
- [ComputeNodeGraph.ValueType.texture(typeName:)](./valuetype/texture%28typename%29.md)
  Value is an texture with the given type name (e.g. texture2d)
### Type Methods
- [static func primitive(MTLDataType) -> ComputeNodeGraph.ValueType](./valuetype/primitive%28_%29.md)
- [static func structure(typeName: String, layout: ComputeNodeGraph.StructureLayout) -> ComputeNodeGraph.ValueType](./valuetype/structure%28typename,layout%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/valuetype)*