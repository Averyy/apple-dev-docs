# ComputeNodeGraph.StructureLayout.Member

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

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
struct Member
```

## Topics

### Initializers
- [init(name: String, type: MTLDataType, offset: Int)](./member/init%28name,type,offset%29.md)
### Instance Properties
- [var dataType: MTLDataType?](./member/datatype.md)
  Data type. For types such as `.struct` and `.pointer`, see [`typeName`](./member/typename.md) and `components` for additional information.
- [var lengthInBytes: Int](./member/lengthinbytes.md)
- [var members: [ComputeNodeGraph.StructureLayout.Member]?](./member/members.md)
- [var name: String](./member/name.md)
  Name of this member in the containing structure
- [var offset: Int](./member/offset.md)
  Offset, in bytes, of this member in its containing structure
- [var type: ComputeNodeGraph.StateType](./member/type.md)
- [var typeName: String?](./member/typename.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/structurelayout/member)*