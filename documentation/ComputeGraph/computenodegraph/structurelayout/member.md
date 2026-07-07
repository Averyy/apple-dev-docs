# ComputeNodeGraph.StructureLayout.Member

**Framework**: Compute Graph  
**Kind**: struct

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
struct Member
```

## Topics

### Initializers
- [init(name: String, type: MTLDataType, offset: Int)](computenodegraph/structurelayout/member/init(name:type:offset:).md)
### Instance Properties
- [var dataType: MTLDataType?](computenodegraph/structurelayout/member/datatype.md)
  Data type. For types such as `.struct` and `.pointer`, see [`typeName`](computenodegraph/structurelayout/member/typename.md) and `components` for additional information.
- [var lengthInBytes: Int](computenodegraph/structurelayout/member/lengthinbytes.md)
- [var members: [ComputeNodeGraph.StructureLayout.Member]?](computenodegraph/structurelayout/member/members.md)
- [var name: String](computenodegraph/structurelayout/member/name.md)
  Name of this member in the containing structure
- [var offset: Int](computenodegraph/structurelayout/member/offset.md)
  Offset, in bytes, of this member in its containing structure
- [var type: ComputeNodeGraph.StateType](computenodegraph/structurelayout/member/type.md)
- [var typeName: String?](computenodegraph/structurelayout/member/typename.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/structurelayout/member)*