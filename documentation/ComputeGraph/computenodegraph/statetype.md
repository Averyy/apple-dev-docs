# ComputeNodeGraph.StateType

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
enum StateType
```

## Topics

### Enumeration Cases
- [case array(definition: ComputeNodeGraph.ArrayDefinition)](computenodegraph/statetype/array(definition:).md)
  Value is an array with the provided definition
- [ComputeNodeGraph.StateType.data(length:)](computenodegraph/statetype/data(length:).md)
  Value is a fixed number of untyped bytes
- [ComputeNodeGraph.StateType.dataType(type:)](computenodegraph/statetype/datatype(type:).md)
  Value is a primitive with the given type
- [case structure(typeName: String, layout: ComputeNodeGraph.StructureLayout)](computenodegraph/statetype/structure(typename:layout:).md)
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