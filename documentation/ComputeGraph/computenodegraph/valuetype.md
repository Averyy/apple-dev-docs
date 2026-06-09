# ComputeNodeGraph.ValueType

**Framework**: ComputeGraph  
**Kind**: enum

Describes the storage and layout of a port’s value, ranging from Metal primitives and structures to opaque references and stateful bindings.

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
enum ValueType
```

## Topics

### Enumeration Cases
- [ComputeNodeGraph.ValueType.data(length:)](computenodegraph/valuetype/data(length:).md)
  Value contains fixed-length data of the given length.
- [ComputeNodeGraph.ValueType.dataType(type:)](computenodegraph/valuetype/datatype(type:).md)
  Value is stored as a metal primitive data type.
- [ComputeNodeGraph.ValueType.enumeration(typeName:)](computenodegraph/valuetype/enumeration(typename:).md)
  Value is from enumeration with the given typeName
- [ComputeNodeGraph.ValueType.none](computenodegraph/valuetype/none.md)
  No storage for this value.
- [ComputeNodeGraph.ValueType.opaque(typeName:)](computenodegraph/valuetype/opaque(typename:).md)
  Value is an opaque value of the given type
- [case pointer(type: ComputeNodeGraph.PointerDefinition)](computenodegraph/valuetype/pointer(type:).md)
  Value is a `strided_buffer<element>`, a flexible method for referencing buffer data.
- [case state(definition: ComputeNodeGraph.StateDefinition)](computenodegraph/valuetype/state(definition:).md)
  Value is a stored state value
- [ComputeNodeGraph.ValueType.string](computenodegraph/valuetype/string.md)
  Value is a utf-8 encoded string
- [case structure(typeName: String, layout: ComputeNodeGraph.StructureLayout)](computenodegraph/valuetype/structure(typename:layout:).md)
  Value is a structure with the given layout
- [ComputeNodeGraph.ValueType.texture(typeName:)](computenodegraph/valuetype/texture(typename:).md)
  Value is an texture with the given type name (e.g. texture2d)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/valuetype)*