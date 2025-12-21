# MTLArgumentType

**Framework**: Metal  
**Kind**: enum

The resource type for an argument of a function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLArgumentType
```

## Topics

### Argument types
- [MTLArgumentType.buffer](mtlargumenttype/buffer.md)
  The argument is a buffer.
- [MTLArgumentType.threadgroupMemory](mtlargumenttype/threadgroupmemory.md)
  The argument is a pointer to threadgroup memory.
- [MTLArgumentType.texture](mtlargumenttype/texture.md)
  The argument is a texture.
- [MTLArgumentType.sampler](mtlargumenttype/sampler.md)
  The argument is a texture sampler.
- [MTLArgumentType.imageblock](mtlargumenttype/imageblock.md)
  The argument is an imageblock.
- [MTLArgumentType.imageblockData](mtlargumenttype/imageblockdata.md)
  The argument is imageblock data.
- [MTLArgumentType.visibleFunctionTable](mtlargumenttype/visiblefunctiontable.md)
  The argument is a visible function table.
- [MTLArgumentType.intersectionFunctionTable](mtlargumenttype/intersectionfunctiontable.md)
  The argument is an intersection function table.
- [MTLArgumentType.primitiveAccelerationStructure](mtlargumenttype/primitiveaccelerationstructure.md)
  The argument is a bottom-level ray tracing acceleraton structure for a set of primitives.
- [MTLArgumentType.instanceAccelerationStructure](mtlargumenttype/instanceaccelerationstructure.md)
  The argument is a top-level ray tracing acceleration structure for a set of instances.
### Initializers
- [init?(rawValue: UInt)](mtlargumenttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLAttribute](mtlattribute.md)
  An object that describes an attribute defined in the stage-in argument for a shader.
- [class MTLVertexAttribute](mtlvertexattribute.md)
  An instance that represents an attribute of a vertex function.
- [class MTLArgument](mtlargument.md)
  Information about an argument of a graphics or compute function.
- [typealias MTLAutoreleasedArgument](mtlautoreleasedargument.md)
  A convenience type alias for an autoreleased argument instance.
- [typealias MTLArgumentAccess](mtlargumentaccess.md)
  Function access restrictions to argument data in the shading language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumenttype)*